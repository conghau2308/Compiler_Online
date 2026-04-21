# Generated from C:/Users/vooco/Documents/PPL_252/ASSIGNMENT_1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSParser import CSParser
else:
    from CSParser import CSParser

# This class defines a complete generic visitor for a parse tree produced by CSParser.

class CSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSParser#list_expression.
    def visitList_expression(self, ctx:CSParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression.
    def visitExpression(self, ctx:CSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression1.
    def visitExpression1(self, ctx:CSParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression2.
    def visitExpression2(self, ctx:CSParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression3.
    def visitExpression3(self, ctx:CSParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression4.
    def visitExpression4(self, ctx:CSParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression5.
    def visitExpression5(self, ctx:CSParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression6.
    def visitExpression6(self, ctx:CSParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression7.
    def visitExpression7(self, ctx:CSParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression8.
    def visitExpression8(self, ctx:CSParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression9.
    def visitExpression9(self, ctx:CSParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression10.
    def visitExpression10(self, ctx:CSParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression11.
    def visitExpression11(self, ctx:CSParser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#function_call.
    def visitFunction_call(self, ctx:CSParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#lhs.
    def visitLhs(self, ctx:CSParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#literal.
    def visitLiteral(self, ctx:CSParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#struct_literal.
    def visitStruct_literal(self, ctx:CSParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#all_type.
    def visitAll_type(self, ctx:CSParser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#primitive_type.
    def visitPrimitive_type(self, ctx:CSParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#var_type.
    def visitVar_type(self, ctx:CSParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#function_type.
    def visitFunction_type(self, ctx:CSParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#list_statement.
    def visitList_statement(self, ctx:CSParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#statement.
    def visitStatement(self, ctx:CSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#var_statement.
    def visitVar_statement(self, ctx:CSParser.Var_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#init_value.
    def visitInit_value(self, ctx:CSParser.Init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#block_statement.
    def visitBlock_statement(self, ctx:CSParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#if_statement.
    def visitIf_statement(self, ctx:CSParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#while_statement.
    def visitWhile_statement(self, ctx:CSParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#for_statement.
    def visitFor_statement(self, ctx:CSParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#for_init.
    def visitFor_init(self, ctx:CSParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#assign_init.
    def visitAssign_init(self, ctx:CSParser.Assign_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#for_update.
    def visitFor_update(self, ctx:CSParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#switch_statement.
    def visitSwitch_statement(self, ctx:CSParser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#case_section.
    def visitCase_section(self, ctx:CSParser.Case_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#default_section.
    def visitDefault_section(self, ctx:CSParser.Default_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#break_statement.
    def visitBreak_statement(self, ctx:CSParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#continue_statement.
    def visitContinue_statement(self, ctx:CSParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#expression_statement.
    def visitExpression_statement(self, ctx:CSParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#return_statement.
    def visitReturn_statement(self, ctx:CSParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#program.
    def visitProgram(self, ctx:CSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#structs.
    def visitStructs(self, ctx:CSParser.StructsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#struct_body.
    def visitStruct_body(self, ctx:CSParser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#explicit_type.
    def visitExplicit_type(self, ctx:CSParser.Explicit_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#functions.
    def visitFunctions(self, ctx:CSParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#list_parameter.
    def visitList_parameter(self, ctx:CSParser.List_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSParser#parameter.
    def visitParameter(self, ctx:CSParser.ParameterContext):
        return self.visitChildren(ctx)



del CSParser