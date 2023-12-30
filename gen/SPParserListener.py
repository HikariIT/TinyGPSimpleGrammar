# Generated from C:/Users/hikar/Desktop/New programming/RnD/SimplerGrammar/grammar\SPParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SPParser import SPParser
else:
    from SPParser import SPParser

# This class defines a complete listener for a parse tree produced by SPParser.
class SPParserListener(ParseTreeListener):

    # Enter a parse tree produced by SPParser#program.
    def enterProgram(self, ctx:SPParser.ProgramContext):
        pass

    # Exit a parse tree produced by SPParser#program.
    def exitProgram(self, ctx:SPParser.ProgramContext):
        pass


    # Enter a parse tree produced by SPParser#block.
    def enterBlock(self, ctx:SPParser.BlockContext):
        pass

    # Exit a parse tree produced by SPParser#block.
    def exitBlock(self, ctx:SPParser.BlockContext):
        pass


    # Enter a parse tree produced by SPParser#statementList.
    def enterStatementList(self, ctx:SPParser.StatementListContext):
        pass

    # Exit a parse tree produced by SPParser#statementList.
    def exitStatementList(self, ctx:SPParser.StatementListContext):
        pass


    # Enter a parse tree produced by SPParser#statement.
    def enterStatement(self, ctx:SPParser.StatementContext):
        pass

    # Exit a parse tree produced by SPParser#statement.
    def exitStatement(self, ctx:SPParser.StatementContext):
        pass


    # Enter a parse tree produced by SPParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:SPParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by SPParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:SPParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by SPParser#ifStatement.
    def enterIfStatement(self, ctx:SPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SPParser#ifStatement.
    def exitIfStatement(self, ctx:SPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SPParser#loopStatement.
    def enterLoopStatement(self, ctx:SPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SPParser#loopStatement.
    def exitLoopStatement(self, ctx:SPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by SPParser#read.
    def enterRead(self, ctx:SPParser.ReadContext):
        pass

    # Exit a parse tree produced by SPParser#read.
    def exitRead(self, ctx:SPParser.ReadContext):
        pass


    # Enter a parse tree produced by SPParser#write.
    def enterWrite(self, ctx:SPParser.WriteContext):
        pass

    # Exit a parse tree produced by SPParser#write.
    def exitWrite(self, ctx:SPParser.WriteContext):
        pass


    # Enter a parse tree produced by SPParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SPParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SPParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#unaryExpression.
    def enterUnaryExpression(self, ctx:SPParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#unaryExpression.
    def exitUnaryExpression(self, ctx:SPParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SPParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SPParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SPParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SPParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SPParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SPParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#equalityExpression.
    def enterEqualityExpression(self, ctx:SPParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#equalityExpression.
    def exitEqualityExpression(self, ctx:SPParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:SPParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:SPParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:SPParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:SPParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#expression.
    def enterExpression(self, ctx:SPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#expression.
    def exitExpression(self, ctx:SPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#castExpression.
    def enterCastExpression(self, ctx:SPParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by SPParser#castExpression.
    def exitCastExpression(self, ctx:SPParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by SPParser#relation.
    def enterRelation(self, ctx:SPParser.RelationContext):
        pass

    # Exit a parse tree produced by SPParser#relation.
    def exitRelation(self, ctx:SPParser.RelationContext):
        pass


    # Enter a parse tree produced by SPParser#equalityRelation.
    def enterEqualityRelation(self, ctx:SPParser.EqualityRelationContext):
        pass

    # Exit a parse tree produced by SPParser#equalityRelation.
    def exitEqualityRelation(self, ctx:SPParser.EqualityRelationContext):
        pass


    # Enter a parse tree produced by SPParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SPParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SPParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SPParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SPParser#literal.
    def enterLiteral(self, ctx:SPParser.LiteralContext):
        pass

    # Exit a parse tree produced by SPParser#literal.
    def exitLiteral(self, ctx:SPParser.LiteralContext):
        pass


    # Enter a parse tree produced by SPParser#identifier.
    def enterIdentifier(self, ctx:SPParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SPParser#identifier.
    def exitIdentifier(self, ctx:SPParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SPParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:SPParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by SPParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:SPParser.TypeSpecifierContext):
        pass



del SPParser