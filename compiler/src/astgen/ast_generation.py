"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from src.CS.CSVisitor import CSVisitor
from src.CS.CSParser import CSParser
from src.utils.nodes import *


class ASTGeneration(CSVisitor):

    # ------------------------------------------------------------------ #
    #  PROGRAM                                                             #
    # ------------------------------------------------------------------ #

    def visitProgram(self, ctx: CSParser.ProgramContext):
        decls = []
        for child in ctx.getChildren():
            if isinstance(child, CSParser.StructsContext):
                decls.append(self.visit(child))
            elif isinstance(child, CSParser.FunctionsContext):
                decls.append(self.visit(child))
        return Program(decls)

    # ------------------------------------------------------------------ #
    #  STRUCTS                                                             #
    # ------------------------------------------------------------------ #

    def visitStructs(self, ctx: CSParser.StructsContext):
        name = ctx.ID().getText()
        members = [self.visit(b) for b in ctx.struct_body()]
        return StructDecl(name=name, members=members)

    def visitStruct_body(self, ctx: CSParser.Struct_bodyContext):
        return MemberDecl(
            member_type=self.visit(ctx.explicit_type()),
            name=ctx.ID().getText()
        )

    def visitExplicit_type(self, ctx: CSParser.Explicit_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return StructType(ctx.ID().getText())

    # ------------------------------------------------------------------ #
    #  FUNCTIONS                                                           #
    # ------------------------------------------------------------------ #
    # grammar: functions: function_type? ID LPAREN list_parameter? RPAREN block_statement;
    # function_type: primitive_type | ID

    def visitFunctions(self, ctx: CSParser.FunctionsContext):
        return_type = self.visit(ctx.function_type()) if ctx.function_type() else None
        name = ctx.ID().getText()
        params = self.visit(ctx.list_parameter()) if ctx.list_parameter() else []
        body = self.visit(ctx.block_statement())
        return FuncDecl(return_type=return_type, name=name, params=params, body=body)

    def visitFunction_type(self, ctx: CSParser.Function_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return StructType(ctx.ID().getText())

    def visitList_parameter(self, ctx: CSParser.List_parameterContext):
        return [self.visit(p) for p in ctx.parameter()]

    def visitParameter(self, ctx: CSParser.ParameterContext):
        return Param(
            param_type=self.visit(ctx.explicit_type()),
            name=ctx.ID().getText()
        )

    # ------------------------------------------------------------------ #
    #  TYPES                                                               #
    # ------------------------------------------------------------------ #

    def visitAll_type(self, ctx: CSParser.All_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.AUTO():
            return None
        else:
            return StructType(ctx.ID().getText())

    def visitPrimitive_type(self, ctx: CSParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return VoidType()

    def visitVar_type(self, ctx: CSParser.Var_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return None
        else:
            return StructType(ctx.ID().getText())

    # ------------------------------------------------------------------ #
    #  STATEMENTS                                                          #
    # ------------------------------------------------------------------ #
    # grammar: statement: var_statement SEMI
    #                   | if_statement | while_statement | for_statement
    #                   | switch_statement | break_statement | continue_statement
    #                   | block_statement | expression_statement | return_statement

    def visitStatement(self, ctx: CSParser.StatementContext):
        if ctx.var_statement():
            return self.visit(ctx.var_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.switch_statement():
            return self.visit(ctx.switch_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
        elif ctx.expression_statement():
            return self.visit(ctx.expression_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())

    # grammar: var_statement: var_type ID (ASSIGN init_value)?
    # grammar: init_value: expression | struct_literal
    def visitVar_statement(self, ctx: CSParser.Var_statementContext):
        var_type = self.visit(ctx.var_type())
        name = ctx.ID().getText()
        init = self.visit(ctx.init_value()) if ctx.init_value() else None
        return VarDecl(var_type=var_type, name=name, init_value=init)

    def visitInit_value(self, ctx: CSParser.Init_valueContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.struct_literal())

    # grammar: block_statement: LBRACE statement* RBRACE
    def visitBlock_statement(self, ctx: CSParser.Block_statementContext):
        stmts = [self.visit(s) for s in ctx.statement()]
        return BlockStmt(stmts)

    def visitIf_statement(self, ctx: CSParser.If_statementContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return IfStmt(condition=condition, then_stmt=then_stmt, else_stmt=else_stmt)

    def visitWhile_statement(self, ctx: CSParser.While_statementContext):
        return WhileStmt(
            condition=self.visit(ctx.expression()),
            body=self.visit(ctx.statement())
        )

    # grammar: for_statement: FOR LPAREN for_init? SEMI expression? SEMI for_update? RPAREN statement
    def visitFor_statement(self, ctx: CSParser.For_statementContext):
        init = self.visit(ctx.for_init()) if ctx.for_init() else None
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        update = self.visit(ctx.for_update()) if ctx.for_update() else None
        body = self.visit(ctx.statement())
        return ForStmt(init=init, condition=condition, update=update, body=body)

    # grammar: for_init: var_statement | assign_init
    # grammar: assign_init: lhs ASSIGN expression
    def visitFor_init(self, ctx: CSParser.For_initContext):
        if ctx.var_statement():
            return self.visit(ctx.var_statement())
        else:
            return ExprStmt(self.visit(ctx.assign_init()))

    def visitAssign_init(self, ctx: CSParser.Assign_initContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expression())
        return AssignExpr(lhs=lhs, rhs=rhs)

    # grammar: for_update: lhs ASSIGN expression
    #                    | (INCRE | DECRE) expression8
    #                    | expression10 (INCRE | DECRE)+
    def visitFor_update(self, ctx: CSParser.For_updateContext):
        first = ctx.getChild(0).getText()

        # lhs ASSIGN expression
        if ctx.lhs() and ctx.ASSIGN():
            return AssignExpr(lhs=self.visit(ctx.lhs()), rhs=self.visit(ctx.expression()))

        # prefix: (INCRE | DECRE) expression8
        if first in ('++', '--') and ctx.expression8():
            return PrefixOp(operator=first, operand=self.visit(ctx.expression8()))

        # postfix: expression10 (INCRE | DECRE)+
        op = ctx.getChild(1).getText()  # '++' hoặc '--'
        return PostfixOp(operator=op, operand=self.visit(ctx.expression10()))

    # grammar: switch_statement: SWITCH LPAREN expression RPAREN
    #            LBRACE case_section* default_section? case_section* RBRACE
    def visitSwitch_statement(self, ctx: CSParser.Switch_statementContext):
        cases = [self.visit(c) for c in ctx.case_section()]
        default = self.visit(ctx.default_section()) if ctx.default_section() else None
        return SwitchStmt(
            expr=self.visit(ctx.expression()),
            cases=cases,
            default_case=default
        )

    def visitCase_section(self, ctx: CSParser.Case_sectionContext):
        stmts = [self.visit(s) for s in ctx.statement()]
        return CaseStmt(expr=self.visit(ctx.expression()), statements=stmts)

    def visitDefault_section(self, ctx: CSParser.Default_sectionContext):
        stmts = [self.visit(s) for s in ctx.statement()]
        return DefaultStmt(stmts)

    def visitBreak_statement(self, ctx: CSParser.Break_statementContext):
        return BreakStmt()

    def visitContinue_statement(self, ctx: CSParser.Continue_statementContext):
        return ContinueStmt()

    def visitExpression_statement(self, ctx: CSParser.Expression_statementContext):
        return ExprStmt(self.visit(ctx.expression()))

    # grammar: return_statement: RETURN init_value? SEMI
    def visitReturn_statement(self, ctx: CSParser.Return_statementContext):
        value = self.visit(ctx.init_value()) if ctx.init_value() else None
        return ReturnStmt(value)

    # ------------------------------------------------------------------ #
    #  EXPRESSIONS                                                         #
    # ------------------------------------------------------------------ #
    # grammar: expression: lhs ASSIGN expression | expression1

    def visitExpression(self, ctx: CSParser.ExpressionContext):
        if ctx.ASSIGN():
            return AssignExpr(
                lhs=self.visit(ctx.lhs()),
                rhs=self.visit(ctx.expression())
            )
        return self.visit(ctx.expression1())

    # grammar: expression1: expression2 (OR expression2)*
    def visitExpression1(self, ctx: CSParser.Expression1Context):
        exprs = ctx.expression2()
        result = self.visit(exprs[0])
        for i in range(1, len(exprs)):
            result = BinaryOp(left=result, operator='||', right=self.visit(exprs[i]))
        return result

    # grammar: expression2: expression3 (AND expression3)*
    def visitExpression2(self, ctx: CSParser.Expression2Context):
        exprs = ctx.expression3()
        result = self.visit(exprs[0])
        for i in range(1, len(exprs)):
            result = BinaryOp(left=result, operator='&&', right=self.visit(exprs[i]))
        return result

    # grammar: expression3: expression4 ((EQ | NEQ) expression4)*
    def visitExpression3(self, ctx: CSParser.Expression3Context):
        exprs = ctx.expression4()
        result = self.visit(exprs[0])
        op_tokens = [ctx.getChild(i) for i in range(1, ctx.getChildCount(), 2)]
        for i, op in enumerate(op_tokens):
            result = BinaryOp(left=result, operator=op.getText(), right=self.visit(exprs[i + 1]))
        return result

    # grammar: expression4: expression5 ((LT | LTE | GT | GTE) expression5)*
    def visitExpression4(self, ctx: CSParser.Expression4Context):
        exprs = ctx.expression5()
        result = self.visit(exprs[0])
        op_tokens = [ctx.getChild(i) for i in range(1, ctx.getChildCount(), 2)]
        for i, op in enumerate(op_tokens):
            result = BinaryOp(left=result, operator=op.getText(), right=self.visit(exprs[i + 1]))
        return result

    # grammar: expression5: expression6 ((PLUS | SUB) expression6)*
    def visitExpression5(self, ctx: CSParser.Expression5Context):
        exprs = ctx.expression6()
        result = self.visit(exprs[0])
        op_tokens = [ctx.getChild(i) for i in range(1, ctx.getChildCount(), 2)]
        for i, op in enumerate(op_tokens):
            result = BinaryOp(left=result, operator=op.getText(), right=self.visit(exprs[i + 1]))
        return result

    # grammar: expression6: expression7 ((MUL | DIV | MOD) expression7)*
    def visitExpression6(self, ctx: CSParser.Expression6Context):
        exprs = ctx.expression7()
        result = self.visit(exprs[0])
        op_tokens = [ctx.getChild(i) for i in range(1, ctx.getChildCount(), 2)]
        for i, op in enumerate(op_tokens):
            result = BinaryOp(left=result, operator=op.getText(), right=self.visit(exprs[i + 1]))
        return result

    # grammar: expression7: (NOT | SUB | PLUS) expression7 | expression8
    def visitExpression7(self, ctx: CSParser.Expression7Context):
        if ctx.expression8():
            return self.visit(ctx.expression8())
        op = ctx.getChild(0).getText()
        return PrefixOp(operator=op, operand=self.visit(ctx.expression7()))

    # grammar: expression8: (INCRE | DECRE) expression8 | expression9
    def visitExpression8(self, ctx: CSParser.Expression8Context):
        if ctx.expression9():
            return self.visit(ctx.expression9())
        op = ctx.getChild(0).getText()
        return PrefixOp(operator=op, operand=self.visit(ctx.expression8()))

    # grammar: expression9: expression10 (INCRE | DECRE)*
    def visitExpression9(self, ctx: CSParser.Expression9Context):
        result = self.visit(ctx.expression10())
        # mỗi (INCRE | DECRE) token bọc thêm một PostfixOp
        for i in range(1, ctx.getChildCount()):
            op = ctx.getChild(i).getText()
            result = PostfixOp(operator=op, operand=result)
        return result

    # grammar: expression10: expression10 ACCESS ID | expression11
    def visitExpression10(self, ctx: CSParser.Expression10Context):
        if ctx.expression11():
            return self.visit(ctx.expression11())
        obj = self.visit(ctx.expression10())
        member = ctx.ID().getText()
        return MemberAccess(obj=obj, member=member)

    # grammar: expression11: literal | struct_literal | function_call | ID | LPAREN expression RPAREN
    def visitExpression11(self, ctx: CSParser.Expression11Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        else:
            return self.visit(ctx.expression())

    # grammar: lhs: expression10 ACCESS ID | ID
    def visitLhs(self, ctx: CSParser.LhsContext):
        if ctx.expression10():
            return MemberAccess(
                obj=self.visit(ctx.expression10()),
                member=ctx.ID().getText()
            )
        return Identifier(ctx.ID().getText())

    # ------------------------------------------------------------------ #
    #  LITERALS & MISC                                                     #
    # ------------------------------------------------------------------ #

    def visitLiteral(self, ctx: CSParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        else:
            return StringLiteral(ctx.STRING_LIT().getText())

    # grammar: struct_literal: LBRACE list_expression? RBRACE
    def visitStruct_literal(self, ctx: CSParser.Struct_literalContext):
        args = self.visit(ctx.list_expression()) if ctx.list_expression() else []
        return StructLiteral(values=args)

    # grammar: list_expression: expression (COMMA expression)*
    def visitList_expression(self, ctx: CSParser.List_expressionContext):
        return [self.visit(e) for e in ctx.expression()]

    # grammar: function_call: ID LPAREN list_expression? RPAREN
    def visitFunction_call(self, ctx: CSParser.Function_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.list_expression()) if ctx.list_expression() else []
        return FuncCall(name=name, args=args)