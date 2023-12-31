import random
from copy import deepcopy


def add_indent(multiline_string: str, indent: int):
    return "\n".join(["\t" * indent + line for line in multiline_string.split("\n")])


def print_tree(x, flag, depth, is_last):
    for i in range(1, depth):
        if flag[i]:
            print("| ", "", "", "", end="")

        else:
            print(" ", "", "", "", end="")

    if depth == 0:
        if isinstance(x, ASTNode):
            print("+---", x.name)
        else:
            print("+---", x)

    elif is_last:
        if isinstance(x, ASTNode):
            print("+---", x.name)
        else:
            print("+---", x)
        flag[depth] = False

    else:
        if isinstance(x, ASTNode):
            print("+---", x.name)
        else:
            print("+---", x)

    it = 0

    if not isinstance(x, ASTNode):
        return

    if type(x) == Identifier or type(x) == Literal:
        return

    for i in x.children:
        it += 1
        print_tree(i, flag, depth + 1, it == (len(x.children) - 1))
    flag[depth] = True


class ASTNode:
    name = 'node'
    parent: str
    pos: int


class Program(ASTNode):
    name = 'program'

    def __init__(self, statements):
        self.children = statements

    def __str__(self):
        return "\n".join([str(statement) for statement in self.children])


class Assignment(ASTNode):
    name = '='

    def __init__(self, identifier, expression):
        self.children = [identifier, expression]

    def __str__(self):
        return str(self.children[0]) + " = " + str(self.children[1]) + ";"


class Identifier(ASTNode):
    def __init__(self, identifier):
        self.name = identifier

    def __str__(self):
        return self.name


class Expression(ASTNode):

    def __str__(self):
        return "expression"


class CastExpression(Expression):
    def __init__(self, expression):
        self.children = [expression]
        self.type = random.choice(["int", "float"])

    def __str__(self):
        return self.type + "(" + str(self.children[0]) + ")"


class BinaryOperation(Expression):
    def __init__(self, left, right, operator):
        self.children = [left, right]
        self.name = operator

    def __str__(self):
        return str(self.children[0]) + " " + self.name + " " + str(self.children[1])


class Loop(ASTNode):
    name = 'while'

    def __init__(self, condition, statements):
        self.children = [condition, *statements]

    def __str__(self):
        return "while (" + str(self.children[0]) + ") {\n" + add_indent(
            '\n'.join([str(child) for child in self.children[1:]]), 1) + "\n}"


class Conditional(ASTNode):
    name = 'if'

    def __init__(self, condition, statements):
        self.children = [condition, *statements]

    def __str__(self):
        return "if (" + str(self.children[0]) + ") {\n" + add_indent(
            '\n'.join([str(child) for child in self.children[1:]]), 1) + "\n}"


class Read(ASTNode):
    name = 'read'

    def __init__(self, identifier):
        self.children = [identifier]

    def __str__(self):
        return "read(" + str(self.children[0]) + ");"


class Write(ASTNode):
    name = 'write'

    def __init__(self, expression):
        self.children = [expression]

    def __str__(self):
        return "write(" + str(self.children[0]) + ");"


class Literal(ASTNode):
    terminating = True

    def __init__(self, literal):
        self.name = literal

    def __str__(self):
        return self.name


class ProgramGenerator:
    initialized_variables = []

    def __init__(self):
        self.DEPTH = 0
        self.MAX_DEPTH = 3
        self.NO_IDENTIFIERS = 10

    def generate_expression(self, in_loop_or_conditional=False):
        self.DEPTH += 1
        if in_loop_or_conditional:
            expression_probabilities = {
                BinaryOperation: 0.97,
                CastExpression: 0.01,
                Identifier: 0.01,
                Literal: 0.01
            }
        else:
            expression_probabilities = {
                BinaryOperation: 0.2,
                CastExpression: 0.1,
                Identifier: 0.35,
                Literal: 0.35
            }

        if self.DEPTH >= self.MAX_DEPTH:
            expression_probabilities = {
                Identifier: 0.5,
                Literal: 0.5
            }

        expression_type = random.choices(list(expression_probabilities.keys()), list(expression_probabilities.values()))[0]
        return_node = None


        if expression_type == BinaryOperation:
            return_node = BinaryOperation(self.generate_expression(), self.generate_expression(),
                                          random.choice(["+", "-", "*", "/", "<", "<=", ">", ">=", "==", "!="]))
        elif expression_type == Identifier:
            return_node = Identifier(self.generate_identifier())
        elif expression_type == Literal:
            return_node = Literal(str(random.randint(-100, 100)))
        elif expression_type == CastExpression:
            return_node = CastExpression(self.generate_expression())

        self.DEPTH -= 1
        return return_node

    def generate_new_identifier(self):
        new_identifier = 'i_' + str(random.randint(0, self.NO_IDENTIFIERS))
        self.initialized_variables.append(new_identifier)
        return new_identifier

    def generate_identifier(self):
        return random.choice(self.initialized_variables)

    def generate_statement(self):
        self.DEPTH += 1

        statement_probabilities = {
            Assignment: 0.3,
            Loop: 0.15,
            Conditional: 0.15,
            Read: 0.2,
            Write: 0.2
        }

        if self.DEPTH >= self.MAX_DEPTH:
            statement_probabilities = {
                Assignment: 0.6,
                Read: 0.2,
                Write: 0.2
            }

        statement_type = random.choices(list(statement_probabilities.keys()), list(statement_probabilities.values()))[0]

        return_node = None

        if statement_type == Assignment:
            return_node = Assignment(Identifier(self.generate_new_identifier()), self.generate_expression())
        elif statement_type == Loop:
            return_node = Loop(self.generate_expression(in_loop_or_conditional=True), self.generate_statements())
        elif statement_type == Conditional:
            return_node = Conditional(self.generate_expression(in_loop_or_conditional=True), self.generate_statements())
        elif statement_type == Read:
            return_node = Read(Identifier(self.generate_new_identifier()))
        elif statement_type == Write:
            return_node = Write(self.generate_expression())

        self.DEPTH -= 1
        return return_node

    def generate_statements(self):
        no_statements = max(1, int(random.randint(1, 5)))
        statements = []

        for _ in range(no_statements):
            statements.append(self.generate_statement())

        return statements

    def generate_program(self):
        return Program([Assignment(Identifier(self.generate_new_identifier()), random.randint(-100, 100)),
                        *self.generate_statements()])


pg = ProgramGenerator()
program = pg.generate_program()
# print(program)
# print_tree(program, [True] * 1000, 0, False)


class GP:

    pg = ProgramGenerator()

    @staticmethod
    def crossover(p_1, p_2):
        p_1_copy = deepcopy(p_1)
        p_2_copy = deepcopy(p_2)

        node_1_parent = p_1_copy
        random_node_1 = random.choice(p_1_copy.children)

        while random.random() > 0.3:
            if not hasattr(random_node_1, 'children') or len(random_node_1.children) == 0:
                break
            node_1_parent = random_node_1
            random_node_1 = random.choice(random_node_1.children)

        repetitions = 0

        node_2_parent = p_2_copy
        random_node_2 = random.choice(p_2_copy.children)
        while type(random_node_2) != type(random_node_1):
            repetitions += 1
            random_node_2 = p_2_copy
            while random.random() > 0.3:
                if not hasattr(random_node_2, 'children') or len(random_node_2.children) == 0:
                    break
                node_2_parent = random_node_2
                random_node_2 = random.choice(random_node_2.children)

            if repetitions > 10:
                print('Crossover failed')
                return p_1_copy, p_2_copy

        print('Crossover of {} and {}'.format(random_node_1, random_node_2))

        # Swap the nodes
        node_1_pos = node_1_parent.children.index(random_node_1)
        node_2_pos = node_2_parent.children.index(random_node_2)

        node_1_parent.children[node_1_pos] = random_node_2
        node_2_parent.children[node_2_pos] = random_node_1

        return p_1_copy, p_2_copy

    @staticmethod
    def mutate(program):
        program_copy = deepcopy(program)
        node_to_mutate = random.choice(program_copy.children)
        node_to_mutate_parent = program_copy
        while random.random() > 0.3:
            if not hasattr(node_to_mutate, 'children') or len(node_to_mutate.children) == 0:
                break
            node_to_mutate_parent = node_to_mutate
            node_to_mutate = random.choice(node_to_mutate.children)

        node_to_mutate_index = node_to_mutate_parent.children.index(node_to_mutate)

        print('Mutating {}'.format(node_to_mutate))
        if type(node_to_mutate) == Assignment:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Assignment(Identifier(GP.pg.generate_new_identifier()), GP.pg.generate_expression()))
        elif type(node_to_mutate) == Loop:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Loop(GP.pg.generate_expression(in_loop_or_conditional=True), GP.pg.generate_statements()))
        elif type(node_to_mutate) == Conditional:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Conditional(GP.pg.generate_expression(in_loop_or_conditional=True), GP.pg.generate_statements()))
        elif type(node_to_mutate) == Read:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Read(Identifier(GP.pg.generate_new_identifier())))
        elif type(node_to_mutate) == Write:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Write(GP.pg.generate_expression()))
        elif type(node_to_mutate) == Identifier:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Identifier(GP.pg.generate_identifier()))
        elif type(node_to_mutate) == Literal:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Literal(str(random.randint(-100, 100))))
        elif type(node_to_mutate) == BinaryOperation:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                BinaryOperation(GP.pg.generate_expression(), GP.pg.generate_expression(),
                                random.choice(["+", "-", "*", "/", "<", "<=", ">", ">=", "==", "!="])))

        return program_copy


program_1 = pg.generate_program()
program_2 = pg.generate_program()

"""
print(program_1)
print('------------------')
print(program_2)
child_1, child_2 = GP.crossover(program_1, program_2)
print(child_1)
print('------------------')
print(child_2)

"""

print(program_1)
print('------------------')
mutated = GP.mutate(program_1)
print(mutated)