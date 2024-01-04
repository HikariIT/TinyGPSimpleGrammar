# Generated from C:/Users/hikar/Desktop/New programming/RnD/SimplerGrammar/grammar\SPParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SPParser import SPParser
else:
    from SPParser import SPParser

# This class defines a complete generic visitor for a parse tree produced by SPParser.

class SPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SPParser#program.
    def visitProgram(self, ctx:SPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#block.
    def visitBlock(self, ctx:SPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#statementList.
    def visitStatementList(self, ctx:SPParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#statement.
    def visitStatement(self, ctx:SPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:SPParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#ifStatement.
    def visitIfStatement(self, ctx:SPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#loopStatement.
    def visitLoopStatement(self, ctx:SPParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#read.
    def visitRead(self, ctx:SPParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#write.
    def visitWrite(self, ctx:SPParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:SPParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#unaryExpression.
    def visitUnaryExpression(self, ctx:SPParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SPParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SPParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#relationalExpression.
    def visitRelationalExpression(self, ctx:SPParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#equalityExpression.
    def visitEqualityExpression(self, ctx:SPParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:SPParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:SPParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#expression.
    def visitExpression(self, ctx:SPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#castExpression.
    def visitCastExpression(self, ctx:SPParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#relation.
    def visitRelation(self, ctx:SPParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#equalityRelation.
    def visitEqualityRelation(self, ctx:SPParser.EqualityRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#unaryOperator.
    def visitUnaryOperator(self, ctx:SPParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#literal.
    def visitLiteral(self, ctx:SPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#identifier.
    def visitIdentifier(self, ctx:SPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:SPParser.TypeSpecifierContext):
        return self.visitChildren(ctx)



del SPParser