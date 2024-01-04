import logging
import utils.logger
from gen.SPParserVisitor import SPParserVisitor
from gen.SPParser import SPParser
from typing import TextIO

from variables.memory import VariableMemory
from variables.variable import Variable


class InterpreterVisitor(SPParserVisitor):
    in_file: TextIO
    out_file: TextIO
    variable_memory: VariableMemory

    def __init__(self, in_path: str, out_path: str):
        super().__init__()
        self.logger = utils.logger.createLogger("Visitor", logging.DEBUG)
        self.logger.info("Visitor initialized")
        self.in_file = open(in_path, "r")
        self.out_file = open(out_path, "w+")
        self.variable_memory = VariableMemory()

    def visitProgram(self, ctx: SPParser.ProgramContext):
        self.visitChildren(ctx)

    def visitBlock(self, ctx: SPParser.BlockContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx: SPParser.StatementContext):
        for child in ctx.children:
            self.visit(child)

    def visitAssignmentStatement(self, ctx: SPParser.AssignmentStatementContext):
        identifier = ctx.identifier().getText()
        value = self.visit(ctx.expression())
        self.variable_memory.assign_variable(identifier, value)

    def visitIfStatement(self, ctx: SPParser.IfStatementContext):
        if ctx.KW_ELSE():
            if self.visit(ctx.expression()):
                self.visit(ctx.statement(0))
            else:
                self.visit(ctx.statement(1))
        else:
            if self.visit(ctx.expression()):
                self.visit(ctx.statement(0))

    def visitLoopStatement(self, ctx: SPParser.LoopStatementContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    def visitRead(self, ctx: SPParser.ReadContext):
        self.logger.debug("Reading from file: " + ctx.identifier().getText())
        identifier = ctx.identifier().getText()
        value = self.in_file.readline()
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                value = 0
        self.variable_memory.assign_variable(identifier, value)

    def visitWrite(self, ctx: SPParser.WriteContext):
        self.variable_memory.operation_count += 1
        if self.variable_memory.operation_count > self.variable_memory.MAX_OPERATIONS:
            raise RecursionError("Too many operations")
        self.logger.debug("Writing to file: " + ctx.expression().getText())
        value = self.visit(ctx.expression())
        self.out_file.write(str(value) + "\n")

    def visitExpression(self, ctx: SPParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitPrimaryExpression(self, ctx: SPParser.PrimaryExpressionContext):
        if ctx.identifier():
            return self.variable_memory.get_variable_value(ctx.identifier().getText())
        elif ctx.literal():
            if ctx.literal().INTEGER_LITERAL():
                return int(ctx.literal().getText())
            elif ctx.literal().FLOAT_LITERAL():
                return float(ctx.literal().getText())

    def visitUnaryExpression(self, ctx: SPParser.UnaryExpressionContext):
        if ctx.unaryOperator():
            value = self.visit(ctx.primaryExpression())
            if ctx.unaryOperator().MINUS():
                return -value
            elif ctx.unaryOperator().NOT():
                return not value
            else:
                return value
        return self.visit(ctx.primaryExpression())

    def visitMultiplicativeExpression(self, ctx: SPParser.MultiplicativeExpressionContext):
        value = self.visit(ctx.unaryExpression()[0])

        for expression in range(1, len(ctx.unaryExpression())):
            if ctx.TIMES():
                value *= self.visit(ctx.unaryExpression()[expression])
            elif ctx.DIV() and self.visit(ctx.unaryExpression()[expression]) != 0:
                value /= self.visit(ctx.unaryExpression()[expression])

        return value

    def visitAdditiveExpression(self, ctx: SPParser.AdditiveExpressionContext):
        if len(ctx.multiplicativeExpression()) == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        value = self.visit(ctx.multiplicativeExpression(0))
        left = Variable.create_and_assign("left", value)

        for i, expression in enumerate(ctx.multiplicativeExpression()[1:]):
            next_value = self.visit(expression)
            right = Variable.create_and_assign("right", next_value)

            if ctx.PLUS():
                result = left.value + right.value
                left.on_assign(result)
            elif ctx.MINUS():
                result = left.value - right.value
                left.on_assign(result)

        return left.value

    def visitRelationalExpression(self, ctx: SPParser.RelationalExpressionContext):
        if len(ctx.additiveExpression()) == 1:
            return self.visit(ctx.additiveExpression(0))

        left_value = self.visit(ctx.additiveExpression(0))
        left = Variable.create_and_assign("left", left_value)

        right_value = self.visit(ctx.additiveExpression(1))
        right = Variable.create_and_assign("right", right_value)

        if ctx.relation().LT():
            return left.value < right.value
        elif ctx.relation().GT():
            return left.value > right.value
        elif ctx.relation().LE():
            return left.value <= right.value
        elif ctx.relation().GE():
            return left.value >= right.value

    def visitEqualityExpression(self, ctx: SPParser.EqualityExpressionContext):
        if len(ctx.relationalExpression()) == 1:
            return self.visit(ctx.relationalExpression(0))

        left_value = self.visit(ctx.relationalExpression(0))
        left = Variable.create_and_assign("left", left_value)

        right_value = self.visit(ctx.relationalExpression(1))
        right = Variable.create_and_assign("right", right_value)

        if ctx.equalityRelation().EQ():
            return left.value == right.value
        elif ctx.equalityRelation().NE():
            return left.value != right.value

        raise Exception("Invalid operator")

    def visitLogicalAndExpression(self, ctx: SPParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) == 1:
            return self.visit(ctx.equalityExpression(0))

        left_value = self.visit(ctx.equalityExpression(0))
        left = Variable.create_and_assign("left", left_value)

        right_value = self.visit(ctx.equalityExpression(1))
        right = Variable.create_and_assign("right", right_value)

        return left.value and right.value

    def visitLogicalOrExpression(self, ctx: SPParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) == 1:
            return self.visit(ctx.logicalAndExpression(0))

        left_value = self.visit(ctx.logicalAndExpression(0))
        left = Variable.create_and_assign("left", left_value)

        right_value = self.visit(ctx.logicalAndExpression(1))
        right = Variable.create_and_assign("right", right_value)
        return left.value or right.value

    def visitCastExpression(self, ctx:SPParser.CastExpressionContext):
        if ctx.typeSpecifier().KW_INT():
            return int(self.visit(ctx.expression()))
        elif ctx.typeSpecifier().KW_FLOAT():
            return float(self.visit(ctx.expression()))
        else:
            return self.visit(ctx.expression())
