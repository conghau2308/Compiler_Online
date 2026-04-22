"""
Code Generator for CS/TyC programming language.
Generates Java bytecode (Jasmin .j format) by traversing the AST.
"""

import os
from typing import Any, Dict, List, Optional, Tuple
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    Program, StructDecl, MemberDecl, FuncDecl, Param, VarDecl,
    IfStmt, WhileStmt, ForStmt, BreakStmt, ContinueStmt, ReturnStmt,
    BlockStmt, SwitchStmt, CaseStmt, DefaultStmt,
    IntType, FloatType, StringType, VoidType, StructType,
    BinaryOp, PrefixOp, PostfixOp, AssignExpr, MemberAccess, FuncCall,
    Identifier, StructLiteral, IntLiteral, FloatLiteral, StringLiteral,
    ExprStmt,
)
from .emitter import Emitter
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException


# ── Environment helpers ────────────────────────────────────────────────────────

class VarInfo:
    """Tracks a local variable: JVM index + type."""
    def __init__(self, index: int, typ):
        self.index = index
        self.typ = typ


class FuncInfo:
    """Tracks a declared function: JVM descriptor + return type."""
    def __init__(self, descriptor: str, return_type):
        self.descriptor = descriptor
        self.return_type = return_type


class StructInfo:
    """Tracks a struct: ordered list of (field_name, type)."""
    def __init__(self, fields: List[Tuple[str, Any]]):
        self.fields = fields   # [(name, type), ...]


# ── Main CodeGenerator ─────────────────────────────────────────────────────────

class CodeGenerator(ASTVisitor):
    """
    Generates Jasmin (.j) bytecode from a TyC/CS AST.

    Environment object `o` passed to visitors is a dict with keys:
        "vars"    : Dict[str, VarInfo]   – local variables in current scope
        "funcs"   : Dict[str, FuncInfo]  – all declared functions
        "structs" : Dict[str, StructInfo]– all declared structs
        "break_label"    : Optional[str] – label to jump to on break
        "continue_label" : Optional[str] – label to jump to on continue
    """

    def __init__(self):
        self.class_name = "CS"
        self.emit: Emitter = Emitter(self.class_name + ".j")
        self.frame: Frame = None
        self._label_counter = 0

    # ── Label helper ──────────────────────────────────────────────────────────

    def _new_label(self) -> str:
        self._label_counter += 1
        return f"L{self._label_counter}"

    def _emit_label(self, label: str) -> None:
        self.emit.print_out(f"{label}:\n")

    def _emit_goto(self, label: str) -> None:
        self.emit.print_out(f"\tgoto {label}\n")

    def _emit_ifeq(self, label: str) -> None:
        """Jump to label if top-of-stack == 0 (false)."""
        self.frame.pop()
        self.emit.print_out(f"\tifeq {label}\n")

    def _emit_ifne(self, label: str) -> None:
        """Jump to label if top-of-stack != 0 (true)."""
        self.frame.pop()
        self.emit.print_out(f"\tifne {label}\n")

    # ── Type helpers ─────────────────────────────────────────────────────────

    def _jvm_type(self, typ) -> str:
        if isinstance(typ, IntType):    return "I"
        if isinstance(typ, FloatType):  return "F"
        if isinstance(typ, StringType): return "Ljava/lang/String;"
        if isinstance(typ, VoidType):   return "V"
        if isinstance(typ, StructType):
            return f"L{self.class_name}${typ.struct_name};"
        return "V"

    def _jvm_descriptor(self, params: List[Param], return_type) -> str:
        param_desc = "".join(self._jvm_type(p.param_type) for p in params)
        ret_desc   = self._jvm_type(return_type) if return_type else "V"
        return f"({param_desc}){ret_desc}"

    def _make_env(self) -> dict:
        return {
            "vars": {},
            "funcs": {},
            "structs": {},
            "break_label": None,
            "continue_label": None,
        }

    def _child_env(self, o: dict) -> dict:
        """Create a child scope that inherits funcs/structs and break/continue labels."""
        return {
            "vars": dict(o["vars"]),   # copy so inner vars don't leak out
            "funcs": o["funcs"],       # shared reference
            "structs": o["structs"],   # shared reference
            "break_label": o.get("break_label"),
            "continue_label": o.get("continue_label"),
        }

    # ── Emit store/load by type ───────────────────────────────────────────────

    def _emit_load(self, typ, index: int) -> None:
        code = self.emit.emit_read_var(typ, index, self.frame)
        self.emit.print_out(code)

    def _emit_store(self, typ, index: int) -> None:
        self.frame.pop()
        if isinstance(typ, FloatType):
            self.emit.print_out(f"\tfstore {index}\n")
        elif isinstance(typ, StringType):
            self.emit.print_out(f"\tastore {index}\n")
        else:
            code = self.emit.emit_write_var(index, self.frame)
            self.frame.push()          # emit_write_var already called pop once
            self.frame.pop()           # undo the push we just did
            self.emit.print_out(code)

    # ── Program ───────────────────────────────────────────────────────────────

    def visit_program(self, node: "Program", o: Any = None):
        self.emit.print_out(self.emit.emit_prolog(self.class_name, "java/lang/Object"))

        env = self._make_env()

        # First pass: collect struct and function signatures
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                self.visit_struct_decl(decl, env)
            elif isinstance(decl, FuncDecl):
                desc = self._jvm_descriptor(decl.params, decl.return_type)
                env["funcs"][decl.name] = FuncInfo(desc, decl.return_type)

        # Second pass: emit function bodies
        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                self.visit_func_decl(decl, env)

        # Constructor - emit thẳng, không dùng Frame
        self.emit.print_out(
            self.emit.emit_method(lexeme="<init>", in_type="()V", is_static=False)
        )
        self.emit.print_out("\t.limit stack 1\n")
        self.emit.print_out("\t.limit locals 1\n")
        self.emit.print_out("\taload_0\n")
        self.emit.print_out("\tinvokespecial java/lang/Object/<init>()V\n")
        self.emit.print_out("\treturn\n")
        self.emit.print_out(".end method\n")

        self.emit.emit_epilog()

    # ── Declarations ─────────────────────────────────────────────────────────

    def visit_struct_decl(self, node: "StructDecl", o: dict):
        fields = [(m.name, m.member_type) for m in node.members]
        o["structs"][node.name] = StructInfo(fields)
        # Emit inner class declaration (Jasmin inner-class workaround via separate class)
        # For simplicity, struct fields are flattened into local vars at use-site.
        return []

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass  # handled inside visit_struct_decl

    def visit_func_decl(self, node: "FuncDecl", o: dict):
        is_main = (node.name == "main")
        if is_main:
            method_type = "([Ljava/lang/String;)V"
        else:
            method_type = self._jvm_descriptor(node.params, node.return_type)

        self.emit.print_out(
            self.emit.emit_method(lexeme=node.name, in_type=method_type, is_static=True)
        )

        self.frame = Frame(node.name)
        self.frame.enter_scope()

        func_env = self._child_env(o)

        # Reserve slots for parameters
        if is_main:
            self.frame.get_new_index()  # args[]
        else:
            for param in node.params:
                idx = self.frame.get_new_index()
                func_env["vars"][param.name] = VarInfo(idx, param.param_type)

        # Visit body
        for stmt in node.body.statements:
            self.visit(stmt, func_env)

        # Ensure every path ends with a return
        if isinstance(node.return_type, VoidType) or node.return_type is None:
            self.emit.print_out(self.emit.emit_return())

        self.emit.print_out(self.emit.emit_end_method(self.frame))
        self.frame.exit_scope()
        return []

    def visit_param(self, node: "Param", o: Any = None):
        pass  # handled in visit_func_decl

    # ── Types (no code emission needed) ──────────────────────────────────────

    def visit_int_type(self, node, o=None):    return IntType()
    def visit_float_type(self, node, o=None):  return FloatType()
    def visit_string_type(self, node, o=None): return StringType()
    def visit_void_type(self, node, o=None):   return VoidType()
    def visit_struct_type(self, node, o=None): return node

    # ── Statements ───────────────────────────────────────────────────────────

    def visit_block_stmt(self, node: "BlockStmt", o: dict):
        child = self._child_env(o)
        for stmt in node.statements:
            self.visit(stmt, child)
            
    def _emit_default_value(self, typ) -> None:
        """Push giá trị mặc định lên stack tương ứng với kiểu dữ liệu."""
        if isinstance(typ, FloatType):
            self.emit.print_out(self.emit.emit_push_fconst(0.0, self.frame))
        elif isinstance(typ, StringType):
            self.emit.print_out(self.emit.emit_ldc_string("", self.frame))
        else:
            # IntType và các kiểu còn lại → default 0
            self.emit.print_out(self.emit.emit_push_iconst(0, self.frame))
            
    def _emit_store(self, typ, index: int) -> None:
        if isinstance(typ, FloatType):
            self.frame.pop()
            self.emit.print_out(f"\tfstore {index}\n")
        elif isinstance(typ, StringType):
            self.frame.pop()
            self.emit.print_out(f"\tastore {index}\n")
        else:
            # emit_write_var tự gọi frame.pop() bên trong — KHÔNG pop thủ công
            code = self.emit.emit_write_var(index, self.frame)
            self.emit.print_out(code)

    def visit_var_decl(self, node: "VarDecl", o: dict):
        idx = self.frame.get_new_index()
        typ = node.var_type if node.var_type else IntType()  # fallback for auto
        o["vars"][node.name] = VarInfo(idx, typ)

        if node.init_value is not None:
            # Có giá trị khởi tạo → visit để push lên stack rồi store
            self._visit_expr(node.init_value, o)
        else:
            # Không có init → push giá trị mặc định để stack không rỗng
            self._emit_default_value(typ)

        self._emit_store(typ, idx)

    def visit_if_stmt(self, node: "IfStmt", o: dict):
        else_label = self._new_label()
        end_label  = self._new_label()

        self._visit_expr(node.condition, o)
        self._emit_ifeq(else_label)         # if condition == 0 → else

        self.visit(node.then_stmt, o)
        self._emit_goto(end_label)

        self._emit_label(else_label)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

        self._emit_label(end_label)

    def visit_while_stmt(self, node: "WhileStmt", o: dict):
        start_label = self._new_label()
        end_label   = self._new_label()

        child = self._child_env(o)
        child["break_label"]    = end_label
        child["continue_label"] = start_label

        self._emit_label(start_label)
        self._visit_expr(node.condition, o)
        self._emit_ifeq(end_label)

        self.visit(node.body, child)
        self._emit_goto(start_label)
        self._emit_label(end_label)

    def visit_for_stmt(self, node: "ForStmt", o: dict):
        start_label    = self._new_label()
        continue_label = self._new_label()
        end_label      = self._new_label()

        child = self._child_env(o)
        child["break_label"]    = end_label
        child["continue_label"] = continue_label

        # init
        if node.init is not None:
            self.visit(node.init, child)

        self._emit_label(start_label)

        # condition
        if node.condition is not None:
            self._visit_expr(node.condition, child)
            self._emit_ifeq(end_label)

        # body
        self.visit(node.body, child)

        # update (continue jumps here)
        self._emit_label(continue_label)
        if node.update is not None:
            self._visit_expr(node.update, child)
            self.frame.pop()   # discard expression result

        self._emit_goto(start_label)
        self._emit_label(end_label)

    def visit_switch_stmt(self, node: "SwitchStmt", o: dict):
        end_label = self._new_label()
        child = self._child_env(o)
        child["break_label"] = end_label

        # Evaluate switch expression
        self._visit_expr(node.expr, o)

        # Build case labels
        case_labels = [self._new_label() for _ in node.cases]
        default_label = self._new_label()

        # Emit tableswitch / lookupswitch (use lookupswitch for safety)
        entries = []
        for i, case in enumerate(node.cases):
            val = case.expr.value  # IntLiteral guaranteed by checker
            entries.append((val, case_labels[i]))

        # Emit lookupswitch
        self.frame.pop()
        lines = ["\tlookupswitch\n"]
        for val, lbl in sorted(entries, key=lambda x: x[0]):
            lines.append(f"\t\t{val} : {lbl}\n")
        lines.append(f"\t\tdefault : {default_label}\n")
        self.emit.print_out("".join(lines))

        for i, case in enumerate(node.cases):
            self._emit_label(case_labels[i])
            self.visit_case_stmt(case, child)

        self._emit_label(default_label)
        if node.default_case:
            self.visit_default_stmt(node.default_case, child)

        self._emit_label(end_label)

    def visit_case_stmt(self, node: "CaseStmt", o: dict):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: dict):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: "BreakStmt", o: dict):
        label = o.get("break_label")
        if label:
            self._emit_goto(label)

    def visit_continue_stmt(self, node: "ContinueStmt", o: dict):
        label = o.get("continue_label")
        if label:
            self._emit_goto(label)

    def visit_return_stmt(self, node: "ReturnStmt", o: dict):
        if node.expr is None:
            self.emit.print_out(self.emit.emit_return())
        else:
            typ = self._visit_expr(node.expr, o)
            if isinstance(typ, FloatType):
                self.frame.pop()
                self.emit.print_out("\tfreturn\n")
            elif isinstance(typ, StringType):
                self.frame.pop()
                self.emit.print_out("\tareturn\n")
            else:
                self.frame.pop()
                self.emit.print_out("\tireturn\n")

    def visit_expr_stmt(self, node: "ExprStmt", o: dict):
        typ = self._visit_expr(node.expr, o)
        # Discard result if any value was left on stack
        if not isinstance(node.expr, AssignExpr):
            if typ is not None and not isinstance(typ, VoidType):
                self.frame.pop()
                self.emit.print_out("\tpop\n")

    # ── Expression dispatch ───────────────────────────────────────────────────

    def _visit_expr(self, node, o: dict):
        """Visit an expression node and return its type."""
        return self.visit(node, o)

    # ── Expressions ──────────────────────────────────────────────────────────

    def visit_binary_op(self, node: "BinaryOp", o: dict):
        op = node.operator

        # Short-circuit logical operators
        if op == "&&":
            return self._emit_logical_and(node, o)
        if op == "||":
            return self._emit_logical_or(node, o)

        lt = self._visit_expr(node.left,  o)
        rt = self._visit_expr(node.right, o)

        # Promote int→float if needed
        if isinstance(lt, FloatType) and isinstance(rt, IntType):
            self.emit.print_out("\ti2f\n"); rt = FloatType()
        elif isinstance(rt, FloatType) and isinstance(lt, IntType):
            # swap trick: can't easily do this without a temp; emit i2f on left
            # In practice the checker ensures both sides match; just cast right
            pass

        use_float = isinstance(lt, FloatType) or isinstance(rt, FloatType)
        self.frame.pop()  # binary op consumes two, pushes one

        arith = {
            "+":  ("\tiadd\n",  "\tfadd\n"),
            "-":  ("\tisub\n",  "\tfsub\n"),
            "*":  ("\timul\n",  "\tfmul\n"),
            "/":  ("\tidiv\n",  "\tfdiv\n"),
            "%":  ("\tirem\n",  None),
        }
        cmp_ops = {"==", "!=", "<", ">", "<=", ">="}

        if op in arith:
            int_instr, float_instr = arith[op]
            if use_float and float_instr:
                self.emit.print_out(float_instr)
                return FloatType()
            else:
                self.emit.print_out(int_instr)
                return IntType()

        if op in cmp_ops:
            return self._emit_comparison(op, use_float)

        raise IllegalOperandException(f"Unknown binary operator: {op}")

    def _emit_logical_and(self, node: "BinaryOp", o: dict):
        false_label = self._new_label()
        end_label   = self._new_label()

        self._visit_expr(node.left, o)
        self._emit_ifeq(false_label)

        self._visit_expr(node.right, o)
        self._emit_ifeq(false_label)

        self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
        self._emit_goto(end_label)
        self._emit_label(false_label)
        self.emit.print_out(self.emit.emit_push_iconst(0, self.frame))
        self._emit_label(end_label)
        return IntType()

    def _emit_logical_or(self, node: "BinaryOp", o: dict):
        true_label = self._new_label()
        end_label  = self._new_label()

        self._visit_expr(node.left, o)
        self._emit_ifne(true_label)

        self._visit_expr(node.right, o)
        self._emit_ifne(true_label)

        self.emit.print_out(self.emit.emit_push_iconst(0, self.frame))
        self._emit_goto(end_label)
        self._emit_label(true_label)
        self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
        self._emit_label(end_label)
        return IntType()

    def _emit_comparison(self, op: str, use_float: bool):
        """Emit comparison: leaves 0 or 1 on stack."""
        true_label = self._new_label()
        end_label  = self._new_label()

        if use_float:
            self.emit.print_out("\tfcmpl\n")  # -1/0/1
            self.frame.pop()

        jvm_branch = {
            "==": "ifeq", "!=": "ifne",
            "<":  "iflt", ">":  "ifgt",
            "<=": "ifle", ">=": "ifge",
        }
        instr = jvm_branch[op]
        if not use_float:
            # integer compare: pop one extra (two already on stack → isub → cmp)
            self.emit.print_out(f"\tisub\n")
            self.frame.pop()

        self.emit.print_out(f"\t{instr} {true_label}\n")
        self.emit.print_out(self.emit.emit_push_iconst(0, self.frame))
        self._emit_goto(end_label)
        self._emit_label(true_label)
        self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
        self._emit_label(end_label)
        return IntType()

    def visit_prefix_op(self, node: "PrefixOp", o: dict):
        op = node.operator

        if op == "!":
            typ = self._visit_expr(node.operand, o)
            false_label = self._new_label()
            end_label   = self._new_label()
            self._emit_ifeq(false_label)
            self.emit.print_out(self.emit.emit_push_iconst(0, self.frame))
            self._emit_goto(end_label)
            self._emit_label(false_label)
            self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
            self._emit_label(end_label)
            return IntType()

        if op == "-":
            typ = self._visit_expr(node.operand, o)
            if isinstance(typ, FloatType):
                self.emit.print_out("\tfneg\n")
            else:
                self.emit.print_out("\tineg\n")
            return typ

        if op == "+":
            return self._visit_expr(node.operand, o)

        if op in ("++", "--"):
            # Load, increment, store, push result
            var_info = self._get_var_info(node.operand, o)
            if var_info:
                self._emit_load(var_info.typ, var_info.index)
                self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
                if op == "++":
                    self.emit.print_out(self.emit.emit_add_op(self.frame))
                else:
                    self.frame.pop()
                    self.emit.print_out("\tisub\n")
                # dup then store
                self.emit.print_out("\tdup\n"); self.frame.push()
                self._emit_store(var_info.typ, var_info.index)
                return var_info.typ
            return IntType()

        raise IllegalOperandException(f"Unknown prefix operator: {op}")

    def visit_postfix_op(self, node: "PostfixOp", o: dict):
        op = node.operator
        if op in ("++", "--"):
            var_info = self._get_var_info(node.operand, o)
            if var_info:
                # Load original value (return this)
                self._emit_load(var_info.typ, var_info.index)
                self.emit.print_out("\tdup\n"); self.frame.push()
                self.emit.print_out(self.emit.emit_push_iconst(1, self.frame))
                if op == "++":
                    self.emit.print_out(self.emit.emit_add_op(self.frame))
                else:
                    self.frame.pop()
                    self.emit.print_out("\tisub\n")
                self._emit_store(var_info.typ, var_info.index)
                return var_info.typ
        raise IllegalOperandException(f"Unknown postfix operator: {op}")

    def visit_assign_expr(self, node: "AssignExpr", o: dict):
        typ = self._visit_expr(node.rhs, o)
        # dup so the value stays on stack as the expression's result
        self.emit.print_out("\tdup\n"); self.frame.push()
        self._store_lvalue(node.lhs, typ, o)
        return typ

    def visit_member_access(self, node: "MemberAccess", o: dict):
        # Structs are laid out as consecutive locals; this is a simplified
        # flat-layout approach: encode member as obj_name$member_name
        obj_name = self._lvalue_name(node.obj)
        key = f"{obj_name}${node.member}"
        var_info = o["vars"].get(key)
        if var_info:
            self._emit_load(var_info.typ, var_info.index)
            return var_info.typ
        return IntType()

    def visit_func_call(self, node: "FuncCall", o: dict):
        # Built-in I/O functions
        builtin_result = self._emit_builtin(node, o)
        if builtin_result is not None:
            return builtin_result

        func_info = o["funcs"].get(node.name)
        for arg in node.args:
            self._visit_expr(arg, o)

        if func_info:
            self.emit.print_out(
                self.emit.emit_invoke_static(
                    f"{self.class_name}/{node.name}",
                    func_info.descriptor,
                    self.frame,
                )
            )
            ret = func_info.return_type
            if ret and not isinstance(ret, VoidType):
                self.frame.push()
            return ret
        return VoidType()

    def _emit_builtin(self, node: "FuncCall", o: dict):
        """Emit calls for built-in read/print functions. Returns type or None."""
        builtins = {
            "printInt":    ("io/writeInt",    "(I)V",                   VoidType()),
            "printFloat":  ("io/writeFloat",  "(F)V",                   VoidType()),
            "printString": ("io/writeString", "(Ljava/lang/String;)V",  VoidType()),
            "readInt":     ("io/readInt",     "()I",                    IntType()),
            "readFloat":   ("io/readFloat",   "()F",                    FloatType()),
            "readString":  ("io/readString",  "()Ljava/lang/String;",   StringType()),
        }
        if node.name not in builtins:
            return None

        lexeme, desc, ret_type = builtins[node.name]
        for arg in node.args:
            self._visit_expr(arg, o)

        self.emit.print_out(
            self.emit.emit_invoke_static(lexeme, desc, self.frame)
        )
        if not isinstance(ret_type, VoidType):
            self.frame.push()
        return ret_type

    def visit_identifier(self, node: "Identifier", o: dict):
        var_info = o["vars"].get(node.name)
        if var_info:
            self._emit_load(var_info.typ, var_info.index)
            return var_info.typ
        return IntType()

    def visit_struct_literal(self, node: "StructLiteral", o: dict):
        # Values are pushed in order; caller is responsible for knowing layout
        last_type = IntType()
        for val in node.values:
            last_type = self._visit_expr(val, o)
        return last_type

    # ── Literals ─────────────────────────────────────────────────────────────

    def visit_int_literal(self, node: "IntLiteral", o=None):
        self.emit.print_out(self.emit.emit_push_iconst(node.value, self.frame))
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o=None):
        self.emit.print_out(self.emit.emit_push_fconst(node.value, self.frame))
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o=None):
        self.emit.print_out(self.emit.emit_ldc_string(node.value, self.frame))
        return StringType()

    # ── Lvalue helpers ───────────────────────────────────────────────────────

    def _get_var_info(self, expr, o: dict) -> Optional[VarInfo]:
        if isinstance(expr, Identifier):
            return o["vars"].get(expr.name)
        if isinstance(expr, MemberAccess):
            key = f"{self._lvalue_name(expr.obj)}${expr.member}"
            return o["vars"].get(key)
        return None

    def _lvalue_name(self, expr) -> str:
        if isinstance(expr, Identifier):
            return expr.name
        if isinstance(expr, MemberAccess):
            return f"{self._lvalue_name(expr.obj)}${expr.member}"
        return "__unknown__"

    def _store_lvalue(self, lhs, typ, o: dict) -> None:
        """Store TOS into the lvalue (Identifier or MemberAccess)."""
        var_info = self._get_var_info(lhs, o)
        if var_info:
            self._emit_store(var_info.typ, var_info.index)