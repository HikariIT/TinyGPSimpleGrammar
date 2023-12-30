from gen.SPLexer import SPLexer
from gen.SPParser import SPParser
from gen.SPParserVisitor import SPParserVisitor
from antlr4 import FileStream, CommonTokenStream
from typing import TextIO
from enum import Enum

class NodeType(Enum):
    PROGRAM = 'program'
    ASSIGNMENT = '='
    IDENTIFIER = 'identifier'


class Node:
    def __init__(self, node_type: NodeType, text: str):
        self.text = text
        self.children = []
        self.node_type = node_type


def print_tree(x, flag, depth, is_last):
    if x is None:
        return

    for i in range(1, depth):
        if flag[i]:
            print("| ", "", "", "", end="")

        else:
            print(" ", "", "", "", end="")

    if depth == 0:
        if type(x) != Node:
            print(x)
        else:
            print(x.text)

    elif is_last:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.text)
        flag[depth] = False

    else:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.text)

    if type(x) != Node:
        return

    it = 0
    for i in x.children:
        it += 1
        print_tree(i, flag, depth + 1, it == (len(x.children) - 1))
    flag[depth] = True


class ASTGenerator(SPParserVisitor):

    def __init__(self):
        self.root = Node(NodeType.PROGRAM, 'program')
        self.current_node = self.root

    # No AST action in program
    def visitProgram(self, ctx: SPParser.ProgramContext):
        self.visitChildren(ctx)

    # No AST action in block
    def visitBlock(self, ctx: SPParser.BlockContext):
        self.visitChildren(ctx)

    # No AST action in statementList
    def visitStatementList(self, ctx: SPParser.StatementListContext):
        self.visitChildren(ctx)

    # No AST action in statement
    def visitStatement(self, ctx: SPParser.StatementContext):
        self.visitChildren(ctx)

    # Creation of new node in assignmentStatement
    def visitAssignmentStatement(self, ctx: SPParser.AssignmentStatementContext):
        assignment_node = Node(NodeType.ASSIGNMENT, '=')
        parent_node = self.current_node

        self.current_node.children.append(assignment_node)
        self.current_node = assignment_node
        self.visit(ctx.identifier())
        self.visit(ctx.expression())

        self.current_node = parent_node

    def visitExpression(self, ctx: SPParser.ExpressionContext):
        self.visitChildren(ctx)

    def visitIdentifier(self, ctx: SPParser.IdentifierContext):
        identifier_node = Node(NodeType.IDENTIFIER, ctx.getText())
        self.current_node.children.append(identifier_node)


def main():
    in_file = FileStream('code.test')
    lexer = SPLexer(in_file)
    stream = CommonTokenStream(lexer)
    parser = SPParser(stream)
    tree = parser.program()

    visitor = ASTGenerator()
    visitor.visit(tree)

    print_tree(visitor.root, [True] * 100, 0, True)


if __name__ == '__main__':
    main()