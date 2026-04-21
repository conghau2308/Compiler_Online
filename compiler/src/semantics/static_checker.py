"""
Static Semantic Checker for TyC Programming Language
"""

from typing import List, Optional, Any, Tuple, Union
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode, Program, StructDecl, MemberDecl, FuncDecl, Param, VarDecl,
    IfStmt, WhileStmt, ForStmt, BreakStmt, ContinueStmt, ReturnStmt,
    BlockStmt, SwitchStmt, CaseStmt, DefaultStmt, Type,
    IntType, FloatType, StringType, VoidType, StructType,
    BinaryOp, PrefixOp, PostfixOp, AssignExpr, MemberAccess, FuncCall,
    Identifier, StructLiteral, IntLiteral, FloatLiteral, StringLiteral,
    ExprStmt, Expr, Stmt, Decl,
)

TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]

from .static_error import (
    StaticError, Redeclared, UndeclaredIdentifier, UndeclaredFunction,
    UndeclaredStruct, TypeCannotBeInferred, TypeMismatchInStatement,
    TypeMismatchInExpression, MustInLoop,
)


class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

class StructTypeInfo:
    def __init__(self, name, members):
        self.name = name
        self.members = members

class FunctionTypeInfo:
    def __init__(self, return_type, params):
        self.return_type = return_type
        self.params = params


BUILTIN_FUNCTIONS = [
    Symbol("readInt",     FunctionTypeInfo(IntType(),    [])),
    Symbol("readFloat",   FunctionTypeInfo(FloatType(),  [])),
    Symbol("readString",  FunctionTypeInfo(StringType(), [])),
    Symbol("printInt",    FunctionTypeInfo(VoidType(),   [("value", IntType())])),
    Symbol("printFloat",  FunctionTypeInfo(VoidType(),   [("value", FloatType())])),
    Symbol("printString", FunctionTypeInfo(VoidType(),   [("value", StringType())])),
]


class StaticChecker(ASTVisitor):

    def __init__(self):
        self._param_names: set = set()

    def check_program(self, node: "Program"):
        self.visit_program(node, None)

    def visit_program(self, node: "Program", o: Any = None):
        global_scope = list(BUILTIN_FUNCTIONS)
        for decl in node.decls:
            global_scope.extend(self.visit(decl, [global_scope]))

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _resolve_type(self, typ, o):
        """Resolve type; raise UndeclaredStruct nếu struct chưa khai báo."""
        name = getattr(typ, "struct_name", None)
        if name is not None:
            if not any(s.name == name and isinstance(s.typ, StructTypeInfo)
                       for scope in reversed(o) for s in scope):
                raise UndeclaredStruct(name)
        return typ

    def _type_match(self, t1, t2) -> bool:
        if type(t1) != type(t2):
            return False
        if isinstance(t1, StructType):
            return t1.struct_name == t2.struct_name
        return True

    def _lookup(self, name: str, env) -> Optional[Symbol]:
        for scope in reversed(env):
            for sym in reversed(scope):
                if sym.name == name:
                    return sym
        return None

    def _lookup_func(self, name: str, env) -> Optional[Symbol]:
        for scope in reversed(env):
            for sym in reversed(scope):
                if sym.name == name and isinstance(sym.typ, FunctionTypeInfo):
                    return sym
        return None

    def _lookup_struct(self, name: str, env) -> Optional[StructTypeInfo]:
        for scope in reversed(env):
            for sym in scope:
                if sym.name == name and isinstance(sym.typ, StructTypeInfo):
                    return sym.typ
        return None

    def _is_lvalue(self, expr) -> bool:
        return isinstance(expr, (Identifier, MemberAccess))

    def _infer_id(self, expr, typ, env) -> None:
        """Set type cho Identifier nếu chưa có (auto x;)."""
        if isinstance(expr, Identifier):
            sym = self._lookup(expr.name, env)
            if sym is not None and sym.typ is None:
                sym.typ = typ

    def _walk_expr(self, expr, env, infer_type=None) -> bool:
        """Walk expression tree để infer hoặc detect unresolved Identifiers.
        - infer_type=None  → chỉ detect (trả về True nếu có unresolved)
        - infer_type=T     → infer unresolved thành T (trả về True nếu thành công)
        """
        if isinstance(expr, Identifier):
            sym = self._lookup(expr.name, env)
            if sym is not None and sym.typ is None:
                if infer_type is not None:
                    sym.typ = infer_type
                return True
            return False
        if isinstance(expr, BinaryOp):
            l = self._walk_expr(expr.left,  env, infer_type)
            r = self._walk_expr(expr.right, env, infer_type)
            return l or r
        if isinstance(expr, (PrefixOp, PostfixOp)):
            return self._walk_expr(expr.operand, env, infer_type)
        if isinstance(expr, AssignExpr):
            l = self._walk_expr(expr.lhs, env, infer_type)
            r = self._walk_expr(expr.rhs, env, infer_type)
            return l or r
        if isinstance(expr, MemberAccess):
            return self._walk_expr(expr.obj, env, infer_type)
        return False

    def _get_simple_type(self, expr, env):
        """Lấy type của literal hoặc Identifier mà không raise."""
        if isinstance(expr, IntLiteral):    return IntType()
        if isinstance(expr, FloatLiteral):  return FloatType()
        if isinstance(expr, StringLiteral): return StringType()
        if isinstance(expr, Identifier):
            sym = self._lookup(expr.name, env)
            return sym.typ if sym else None
        return None

    def _infer_for_float(self, expr, env) -> bool:
        """Cố infer operand None trong expr thành float khi result là float.
        Trả về True nếu infer được, False nếu ambiguous.
        
        Chỉ infer được khi bên đã biết là FloatType (float + ? → ? = float).
        Nếu bên đã biết là IntType (int + ?) → ambiguous, không infer.
        """
        if isinstance(expr, Identifier):
            self._infer_id(expr, FloatType(), env)
            return True
        if not isinstance(expr, BinaryOp) or expr.operator not in ("+", "-", "*", "/"):
            return False
        lt = self._get_simple_type(expr.left,  env)
        rt = self._get_simple_type(expr.right, env)

        # Chỉ infer khi bên đã biết là FloatType
        if lt is None and isinstance(rt, FloatType):
            return self._infer_for_float(expr.left, env)
        if rt is None and isinstance(lt, FloatType):
            return self._infer_for_float(expr.right, env)

        return False  # int+? hoặc cả hai None → ambiguous

    def _is_ambiguous_arith(self, expr, env) -> bool:
        """Trả về True nếu expr là BinaryOp +/-/*// mà cả hai nhánh đều None
        → không thể suy diễn duy nhất kiểu của operands.
        """
        if not isinstance(expr, BinaryOp):
            return False
        if expr.operator not in ("+", "-", "*", "/"):
            return False
        lt = self._get_simple_type(expr.left,  env)
        rt = self._get_simple_type(expr.right, env)
        return lt is None and rt is None

    def _resolve_none_init(self, init_expr, declared_type, env, error_node):
        if isinstance(declared_type, IntType):
            # Nếu đích là int, mà biểu thức là ? + ? -> Nhập nhằng
            if self._is_ambiguous_arith(init_expr, env):
                raise TypeCannotBeInferred(error_node)
            # Nếu là int + ?, an toàn suy diễn ? thành int
            self._walk_expr(init_expr, env, IntType())
        else:
            # Đối với FloatType, StringType, StructType...
            # Chỉ suy diễn được nếu nó là một phép gán trực tiếp: auto b; float c = b;
            if isinstance(init_expr, Identifier):
                self._infer_id(init_expr, declared_type, env)
            else:
                # Nếu là biểu thức toán học (b + a), không thể suy diễn -> Quăng lỗi cho chính biểu thức đó
                raise TypeCannotBeInferred(error_node)

    def _infer_condition(self, cond, o):
        """Visit condition; nếu None thì infer → int. Trả về cond_type."""
        env = o[0]
        cond_type = self.visit(cond, o)
        if cond_type is None:
            self._infer_id(cond, IntType(), env)
            cond_type = IntType()
        return cond_type

    # ── Declarations ─────────────────────────────────────────────────────────

    def visit_struct_decl(self, node: "StructDecl", o) -> List[Symbol]:
        current_scope = o[-1]
        if any(s.name == node.name and isinstance(s.typ, StructTypeInfo) for s in current_scope):
            raise Redeclared("Struct", node.name)

        seen, members = [], []
        for m in node.members:
            if m.name in seen:
                raise Redeclared("Member", m.name)
            seen.append(m.name)
            members.append((m.name, self._resolve_type(m.member_type, o)))

        return [Symbol(node.name, StructTypeInfo(node.name, members))]

    def visit_member_decl(self, node, o=None): pass

    def visit_func_decl(self, node: "FuncDecl", o) -> List[Symbol]:
        current_scope = o[-1]
        if any(s.name == node.name and isinstance(s.typ, FunctionTypeInfo) for s in current_scope):
            raise Redeclared("Function", node.name)

        func_scope = []
        for param in node.params:
            func_scope.append(self.visit(param, (o, func_scope)))

        return_type = self._resolve_type(node.return_type, o) if node.return_type else None
        func_type = FunctionTypeInfo(return_type, [(s.name, s.typ) for s in func_scope])

        # Pre-register hàm vào scope TRƯỚC khi visit body → cho phép recursive calls
        self_symbol = Symbol(node.name, func_type)
        current_scope.append(self_symbol)

        new_env = o + [func_scope]
        prev = self._param_names
        self._param_names = {s.name for s in func_scope}

        for stmt in node.body.statements:
            syms = self.visit(stmt, (new_env, func_type, False, False))
            if syms:
                func_scope.extend(syms)

        self._param_names = prev

        if any(s.typ is None for s in func_scope):
            raise TypeCannotBeInferred(node.body)
        if func_type.return_type is None:
            func_type.return_type = VoidType()

        # Trả về [] vì đã add trực tiếp vào current_scope
        return []

    def visit_param(self, node: "Param", o) -> Symbol:
        env, func_scope = o
        if any(s.name == node.name for s in func_scope):
            raise Redeclared("Parameter", node.name)
        return Symbol(node.name, self._resolve_type(node.param_type, env))

    # ── Types ────────────────────────────────────────────────────────────────

    def visit_int_type(self, node, o=None):    return IntType()
    def visit_float_type(self, node, o=None):  return FloatType()
    def visit_string_type(self, node, o=None): return StringType()
    def visit_void_type(self, node, o=None):   return VoidType()
    def visit_struct_type(self, node, o=None): return node

    # ── Statements ───────────────────────────────────────────────────────────

    def visit_block_stmt(self, node: "BlockStmt", o) -> List[Symbol]:
        env, func_type, in_loop, in_switch = o
        local_scope = []
        new_env = env + [local_scope]
        for stmt in node.statements:
            syms = self.visit(stmt, (new_env, func_type, in_loop, in_switch))
            if syms:
                local_scope.extend(syms)
        if any(s.typ is None for s in local_scope):
            raise TypeCannotBeInferred(node)
        return []

    def visit_var_decl(self, node: "VarDecl", o) -> List[Symbol]:
        env, func_type, in_loop, in_switch = o
        current_scope = env[-1]

        if any(s.name == node.name for s in current_scope):
            raise Redeclared("Variable", node.name)
        if node.name in self._param_names:
            raise Redeclared("Variable", node.name)

        # ── auto ──
        if node.var_type is None:
            if node.init_value is None:
                return [Symbol(node.name, None)]
            if isinstance(node.init_value, StructLiteral):
                raise TypeCannotBeInferred(node.init_value)
            inferred = self.visit(node.init_value, o)
            if inferred is None:
                if inferred is None:
                    # Nếu biểu thức init không thể tự xác định kiểu (vd: a + b), ném lỗi ngay
                    raise TypeCannotBeInferred(node.init_value)
            return [Symbol(node.name, inferred)]

        # ── explicit type ──
        declared = self._resolve_type(node.var_type, env)
        if node.init_value is not None:
            if isinstance(node.init_value, StructLiteral):
                self._visit_struct_literal_with_context(node.init_value, declared, o)
            else:
                init_type = self.visit(node.init_value, o)
                if init_type is None:
                    try:
                        self._resolve_none_init(node.init_value, declared, env, node.init_value)
                    except TypeMismatchInStatement:
                        raise TypeMismatchInStatement(node)
                else:
                    # ← FIX: kiểm tra type match khi init_type đã resolve được
                    if not self._type_match(declared, init_type):
                        raise TypeMismatchInStatement(node)
        return [Symbol(node.name, declared)]

    def _visit_stmt_with_new_scope(self, stmt, o):
        """Bọc stmt trong scope ảo nếu không phải BlockStmt."""
        if isinstance(stmt, BlockStmt):
            self.visit(stmt, o)
        else:
            env, func_type, in_loop, in_switch = o
            temp = []
            syms = self.visit(stmt, (env + [temp], func_type, in_loop, in_switch))
            if syms:
                temp.extend(syms)

    def visit_if_stmt(self, node: "IfStmt", o) -> List[Symbol]:
        cond_type = self._infer_condition(node.condition, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self._visit_stmt_with_new_scope(node.then_stmt, o)
        if node.else_stmt:
            self._visit_stmt_with_new_scope(node.else_stmt, o)
        return []

    def visit_while_stmt(self, node: "WhileStmt", o) -> List[Symbol]:
        env, func_type, in_loop, in_switch = o
        cond_type = self._infer_condition(node.condition, o)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self._visit_stmt_with_new_scope(node.body, (env, func_type, True, in_switch))
        return []

    def visit_for_stmt(self, node: "ForStmt", o) -> List[Symbol]:
        env, func_type, in_loop, in_switch = o
        new_o = (env, func_type, True, in_switch)

        # ── 1. init (Không giới hạn kiểu) ──
        if node.init is not None:
            syms = self.visit(node.init, new_o)
            if syms:
                env[-1].extend(syms) 
            
            # (Đã xóa các dòng kiểm tra IntType và raise TypeMismatchInStatement ở đây)

        # ── 2. condition (Bắt buộc là kiểu int/boolean tùy quy định) ──
        if node.condition is not None:
            cond_type = self._infer_condition(node.condition, new_o)
            if not isinstance(cond_type, IntType):
                raise TypeMismatchInStatement(node)

        # ── 3. update (Không giới hạn kiểu) ──
        if node.update is not None:
            self.visit(node.update, new_o)
            # (Bạn cũng nên kiểm tra xem code cũ của bạn có đang ép update phải là IntType không, 
            # nếu có thì hãy gỡ bỏ tương tự như với init)

        # ── 4. body ──
        self._visit_stmt_with_new_scope(node.body, new_o)
        
        return []

    def _is_const_int_expr(self, expr) -> bool:
        """Kiểm tra expression chỉ gồm int literals + operators, không có variable."""
        if isinstance(expr, IntLiteral):
            return True
        if isinstance(expr, FloatLiteral) or isinstance(expr, StringLiteral):
            return False
        if isinstance(expr, (Identifier, FuncCall, MemberAccess)):
            return False  # ← variable/function không được phép
        if isinstance(expr, PrefixOp):
            return self._is_const_int_expr(expr.operand)
        if isinstance(expr, BinaryOp):
            return self._is_const_int_expr(expr.left) and self._is_const_int_expr(expr.right)
        return False

    def visit_switch_stmt(self, node: "SwitchStmt", o) -> List[Symbol]:
        env, func_type, in_loop, in_switch = o

        expr_type = self._infer_condition(node.expr, o)
        if not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)

        switch_scope = []
        new_env = env + [switch_scope]
        case_o = (new_env, func_type, in_loop, True)

        for case in node.cases:
            # 1. Phân giải biểu thức trước để bắt UndeclaredIdentifier, TypeCannotBeInferred...
            case_expr_type = self.visit(case.expr, case_o)
            
            # 2. Kiểm tra kiểu dữ liệu trả về phải là Int
            if not isinstance(case_expr_type, IntType):
                raise TypeMismatchInStatement(node)
                
            # 3. Kiểm tra ràng buộc hằng số (không được phép chứa biến, hàm...)
            if not self._is_const_int_expr(case.expr):
                raise TypeMismatchInStatement(node)
            
            # Tiếp tục duyệt các statement bên trong case
            syms = self.visit(case, case_o)
            if syms:
                switch_scope.extend(syms)

        if node.default_case:
            syms = self.visit(node.default_case, case_o)
            if syms:
                switch_scope.extend(syms)

        if any(s.typ is None for s in switch_scope):
            raise TypeCannotBeInferred(node)
        return []

    def visit_case_stmt(self, node: "CaseStmt", o) -> List[Symbol]:
        env = o[0]
        result = []
        for stmt in node.statements:
            syms = self.visit(stmt, o)
            if syms:
                env[-1].extend(syms)
                result.extend(syms)
        return result

    def visit_default_stmt(self, node: "DefaultStmt", o) -> List[Symbol]:
        env = o[0]
        result = []
        for stmt in node.statements:
            syms = self.visit(stmt, o)
            if syms:
                env[-1].extend(syms)
                result.extend(syms)
        return result

    def visit_break_stmt(self, node: "BreakStmt", o) -> List[Symbol]:
        if not o[2] and not o[3]:
            raise MustInLoop(node)
        return []

    def visit_continue_stmt(self, node: "ContinueStmt", o) -> List[Symbol]:
        if not o[2]:
            raise MustInLoop(node)
        return []

    def visit_return_stmt(self, node: "ReturnStmt", o) -> List[Symbol]:
        env, func_type, *_ = o

        if node.expr is None:
            if func_type.return_type is None:
                func_type.return_type = VoidType()
            elif not isinstance(func_type.return_type, VoidType):
                raise TypeMismatchInStatement(node)
            return []

        # ── non-void return ──
        if isinstance(node.expr, StructLiteral):
            if func_type.return_type is None:
                raise TypeCannotBeInferred(node)
            self._visit_struct_literal_with_context(node.expr, func_type.return_type, o)
            return []

        expr_type = self.visit(node.expr, o)

        if expr_type is None:
            if func_type.return_type is None:
                raise TypeCannotBeInferred(node)
            self._resolve_none_init(node.expr, func_type.return_type, env, node.expr)
            expr_type = func_type.return_type
        elif self._walk_expr(node.expr, env):
            raise TypeCannotBeInferred(node.expr)

        if func_type.return_type is None:
            func_type.return_type = expr_type
        elif not self._type_match(func_type.return_type, expr_type):
            raise TypeMismatchInStatement(node)
        return []

    def visit_expr_stmt(self, node: "ExprStmt", o) -> List[Symbol]:
        env = o[0]
        if isinstance(node.expr, AssignExpr):
            try:
                result = self.visit(node.expr, o)
            except TypeMismatchInExpression as e:
                if e.expr is node.expr:
                    raise TypeMismatchInStatement(node)
                raise  # nested → giữ nguyên TypeMismatchInExpression
        else:
            result = self.visit(node.expr, o)

        if result is None:
            if not self._try_infer_expr_stmt(node.expr, env):
                raise TypeCannotBeInferred(node.expr)
        return []

    def _try_infer_expr_stmt(self, expr, env) -> bool:
        """Cố infer unresolved identifiers trong standalone expression.
        Trả về True nếu infer thành công, False nếu ambiguous.
        """
        # Standalone arithmetic operations like `a + b;` cannot resolve 
        # an unknown operand because `int + int` and `int + float` are both valid.
        if isinstance(expr, BinaryOp) and expr.operator in ("+", "-", "*", "/"):
            # We can only return True if BOTH sides are already known, 
            # meaning no inference was actually needed.
            lt = self._get_simple_type(expr.left, env)
            rt = self._get_simple_type(expr.right, env)
            if lt is not None and rt is not None:
                return True
                
            # If either side is None, it's ambiguous.
            return False 
            
        return False

    # ── Expressions ──────────────────────────────────────────────────────────

    def visit_binary_op(self, node: "BinaryOp", o):
        env = o[0]
        # Đánh giá vế trái
        if isinstance(node.left, StructLiteral):
            lt = "struct_literal"
        else:
            lt = self.visit(node.left, o)
            
        # Đánh giá vế phải
        if isinstance(node.right, StructLiteral):
            rt = "struct_literal"
        else:
            rt = self.visit(node.right, o)
            
        # Nếu có bất kỳ toán hạng nào là StructLiteral -> Lỗi TypeMismatch
        if lt == "struct_literal" or rt == "struct_literal":
            raise TypeMismatchInExpression(node)
        
        op = node.operator

        if op in ("&&", "||"):
            if lt is None:
                if not isinstance(node.left, Identifier):
                    raise TypeCannotBeInferred(node.left)
                self._infer_id(node.left, IntType(), env)
                lt = IntType()
            if rt is None:
                if not isinstance(node.right, Identifier):
                    raise TypeCannotBeInferred(node.right)
                self._infer_id(node.right, IntType(), env)
                rt = IntType()
            if not isinstance(lt, IntType) or not isinstance(rt, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()

        if op == "%":
            if lt is None:
                if not isinstance(node.left, Identifier):
                    raise TypeCannotBeInferred(node.left)
                self._infer_id(node.left, IntType(), env)
                lt = IntType()
            if rt is None:
                if not isinstance(node.right, Identifier):
                    raise TypeCannotBeInferred(node.right)
                self._infer_id(node.right, IntType(), env)
                rt = IntType()
            if not isinstance(lt, IntType) or not isinstance(rt, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()

        if op in ("+", "-", "*", "/"):
            if lt is not None and not isinstance(lt, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            if rt is not None and not isinstance(rt, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            
            if lt is None and rt is None:
                return None

            # ── CHỈ SUY DIỄN KIỂU TỪ INTLITERAL ──
            if lt is None:
                if isinstance(node.right, IntLiteral):
                    self._infer_id(node.left, IntType(), env)
                    lt = IntType()
            elif rt is None:
                if isinstance(node.left, IntLiteral):
                    self._infer_id(node.right, IntType(), env)
                    rt = IntType()

            # Nếu một vế là None, kiểm tra vế còn lại
            if lt is None or rt is None:
                known = lt if lt is not None else rt
                if isinstance(known, FloatType):
                    # Nếu vế đã biết là FloatType mà vế kia là auto -> Nhập nhằng (float + ?)
                    raise TypeCannotBeInferred(node)
                return None 

            return IntType() if isinstance(lt, IntType) and isinstance(rt, IntType) else FloatType()

        if op in ("==", "!=", "<", ">", "<=", ">="):
            # 🛑 ĐÃ XÓA: Bỏ toàn bộ logic suy diễn (infer) từ Literal ở đây
            
            # Nếu có bất kỳ vế nào chưa rõ kiểu (auto), báo lỗi ngay lập tức
            if lt is None or rt is None:
                raise TypeCannotBeInferred(node)
                
            # Cả 2 vế phải là kiểu số (int hoặc float)
            if not isinstance(lt, (IntType, FloatType)) or not isinstance(rt, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
                
            # Phép so sánh luôn trả về IntType (đóng vai trò boolean)
            return IntType()

        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o) -> TyCType:
        ot = self.visit(node.operand, o)
        op = node.operator
        if op in ("+", "-"):
            if ot is None: raise TypeCannotBeInferred(node)
            if not isinstance(ot, (IntType, FloatType)): raise TypeMismatchInExpression(node)
            return ot
        if op == "!":
            if ot is None: self._infer_id(node.operand, IntType(), o[0]); ot = IntType()
            if not isinstance(ot, IntType): raise TypeMismatchInExpression(node)
            return IntType()
        if op in ("++", "--"):
            if not self._is_lvalue(node.operand): raise TypeMismatchInExpression(node)
            if ot is None: self._infer_id(node.operand, IntType(), o[0]); ot = IntType()
            if not isinstance(ot, IntType): raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o) -> TyCType:
        ot = self.visit(node.operand, o)
        op = node.operator
        if op in ("++", "--"):
            if not self._is_lvalue(node.operand): raise TypeMismatchInExpression(node)
            if ot is None: self._infer_id(node.operand, IntType(), o[0]); ot = IntType()
            if not isinstance(ot, IntType): raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o) -> TyCType:
        env = o[0]
        rhs_type = self.visit(node.rhs, o)

        if isinstance(node.lhs, Identifier):
            sym = self._lookup(node.lhs.name, env)
            if sym is None: raise UndeclaredIdentifier(node.lhs.name)
            if isinstance(sym.typ, FunctionTypeInfo): raise UndeclaredIdentifier(node.lhs.name)
            if sym.typ is None:
                if rhs_type is None: raise TypeCannotBeInferred(node)
                sym.typ = rhs_type
                return rhs_type
            lhs_type = sym.typ
        else:
            lhs_type = self.visit(node.lhs, o)

        if rhs_type is None:
            self._resolve_none_init(node.rhs, lhs_type, env, node.rhs)
            return lhs_type
        if self._walk_expr(node.rhs, env):
            raise TypeCannotBeInferred(node.rhs)
        if not self._type_match(lhs_type, rhs_type):
            raise TypeMismatchInExpression(node)
        return lhs_type

    def visit_identifier(self, node: "Identifier", o) -> TyCType:
        sym = self._lookup(node.name, o[0])
        if sym is None: raise UndeclaredIdentifier(node.name)
        if isinstance(sym.typ, FunctionTypeInfo): raise UndeclaredIdentifier(node.name)
        return sym.typ

    def visit_member_access(self, node: "MemberAccess", o) -> TyCType:
        obj_type = self.visit(node.obj, o)
        if not isinstance(obj_type, StructType): raise TypeMismatchInExpression(node)
        info = self._lookup_struct(obj_type.struct_name, o[0])
        if info is None: raise UndeclaredStruct(obj_type.struct_name)
        for mname, mtype in info.members:
            if mname == node.member:
                return mtype
        raise TypeMismatchInExpression(node)

    def visit_func_call(self, node: "FuncCall", o) -> TyCType:
        env = o[0]
        sym = self._lookup_func(node.name, env)
        if sym is None: raise UndeclaredFunction(node.name)
        fn = sym.typ

        if len(node.args) != len(fn.params):
            raise TypeMismatchInExpression(node)

        for arg, (_, param_type) in zip(node.args, fn.params):
            if isinstance(arg, StructLiteral):
                self._visit_struct_literal_with_context(arg, param_type, o)
                arg_type = param_type
            else:
                arg_type = self.visit(arg, o)
                if arg_type is None:
                    self._resolve_none_init(arg, param_type, env, arg)
                    arg_type = param_type
                elif self._walk_expr(arg, env):
                    raise TypeCannotBeInferred(arg)
            if not self._type_match(arg_type, param_type):
                raise TypeMismatchInExpression(node)

        if fn.return_type is None:
            raise TypeCannotBeInferred(node)
        return fn.return_type

    def visit_struct_literal(self, node: "StructLiteral", o) -> TyCType:
        raise TypeCannotBeInferred(node)

    def _visit_struct_literal_with_context(self, node: "StructLiteral", ctx, o) -> TyCType:
        env = o[0]
        if not isinstance(ctx, StructType): raise TypeMismatchInExpression(node)
        info = self._lookup_struct(ctx.struct_name, env)
        if info is None: raise UndeclaredStruct(ctx.struct_name)
        if len(node.values) != len(info.members): raise TypeMismatchInExpression(node)
        
        for elem, (_, mtype) in zip(node.values, info.members):
            if isinstance(elem, StructLiteral):
                et = self._visit_struct_literal_with_context(elem, mtype, o)
            else:
                et = self.visit(elem, o)
                
                # 🛑 ĐOẠN CODE SỬA LỖI: Thêm logic suy diễn kiểu (Inference)
                if et is None:
                    # Cố gắng infer `elem` dựa trên kiểu `mtype` mà struct đòi hỏi
                    self._resolve_none_init(elem, mtype, env, node)
                    et = mtype
                elif self._walk_expr(elem, env):
                    # Nếu có biểu thức phức tạp chứa None không infer được trực tiếp
                    raise TypeCannotBeInferred(elem)
                    
            # Sau khi đã infer, mới tiến hành match type
            if not self._type_match(et, mtype): 
                raise TypeMismatchInExpression(node)
                
        return ctx

    # ── Literals ─────────────────────────────────────────────────────────────

    def visit_int_literal(self, node, o=None):    return IntType()
    def visit_float_literal(self, node, o=None):  return FloatType()
    def visit_string_literal(self, node, o=None): return StringType()