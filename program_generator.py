import random
from copy import deepcopy
import traceback

import numpy as np
from antlr4 import InputStream, CommonTokenStream

from gen.SPLexer import SPLexer
from gen.SPParser import SPParser
from metrics import Metric, MetricType
from visitor import InterpreterVisitor


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


class ParenExpression(Expression):
    def __init__(self, expression):
        self.children = [expression]

    def __str__(self):
        return "(" + str(self.children[0]) + ")"


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

    def __init__(self, identifiers: list[str]):
        self.DEPTH = 0
        self.MAX_DEPTH = 3
        self.identifiers = identifiers

    def generate_literal(self):
        return str(random.randint(-1000, 1000))

    def generate_expression(self):
        return self.generate_or_expression()

    def generate_or_expression(self):
        choice = random.random()
        if choice < 0.03 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_and_expression(), self.generate_and_expression(), "||")
            self.DEPTH -= 1
        else:
            return_node = self.generate_and_expression()

        return return_node

    def generate_and_expression(self):
        choice = random.random()
        if choice < 0.03 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_equality_expression(), self.generate_equality_expression(), "&&")
            self.DEPTH -= 1
        else:
            return_node = self.generate_equality_expression()

        return return_node

    def generate_equality_expression(self):
        choice = random.random()
        if choice < 0.05 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_relational_expression(), self.generate_relational_expression(),
                                          random.choice(["==", "!="]))
            self.DEPTH -= 1
        else:
            return_node = self.generate_relational_expression()

        return return_node

    def generate_relational_expression(self):
        choice = random.random()
        if choice < 0.05 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_additive_expression(), self.generate_additive_expression(),
                                          random.choice(["<", "<=", ">", ">="]))
            self.DEPTH -= 1
        else:
            return_node = self.generate_additive_expression()

        return return_node

    def generate_additive_expression(self):
        choice = random.random()
        if choice < 0.3 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_multiplicative_expression(),
                                          self.generate_multiplicative_expression(),
                                          random.choice(["+", "-"]))
            self.DEPTH -= 1
        else:
            return_node = self.generate_multiplicative_expression()

        return return_node

    def generate_multiplicative_expression(self):
        choice = random.random()

        if choice < 0.3 and self.DEPTH < self.MAX_DEPTH:
            self.DEPTH += 1
            return_node = BinaryOperation(self.generate_primary_expression(),
                                          self.generate_primary_expression(),
                                          random.choice(["*", "/"]))
            self.DEPTH -= 1
        else:
            return_node = self.generate_primary_expression()

        return return_node

    def generate_primary_expression(self):
        self.DEPTH += 1
        expression_probabilities = {
            BinaryOperation: 0.2,
            CastExpression: 0.2,
            Identifier: 0.2,
            Literal: 0.2,
            ParenExpression: 0.2
        }

        if self.DEPTH >= self.MAX_DEPTH:
            expression_probabilities = {
                Identifier: 0.5,
                Literal: 0.5
            }

        expression_type = random.choices(list(expression_probabilities.keys()),
                                         list(expression_probabilities.values()))[0]
        return_node = None

        if expression_type == BinaryOperation:
            return_node = self.generate_or_expression()
        elif expression_type == Identifier:
            return_node = Identifier(self.generate_identifier())
        elif expression_type == Literal:
            return_node = Literal(self.generate_literal())
        elif expression_type == CastExpression:
            return_node = CastExpression(self.generate_expression())
        elif expression_type == ParenExpression:
            return_node = ParenExpression(self.generate_expression())

        self.DEPTH -= 1
        return return_node

    def generate_new_identifier(self):
        new_identifier = random.choice(self.identifiers)
        self.initialized_variables.append(new_identifier)
        return new_identifier

    def generate_identifier(self):
        return random.choice(self.initialized_variables)

    def generate_statement(self):
        self.DEPTH += 1

        statement_probabilities = {
            Assignment: 0.2,
            Loop: 0.1,
            Conditional: 0.1,
            Read: 0.2,
            Write: 0.4
        }

        if self.DEPTH >= self.MAX_DEPTH:
            statement_probabilities = {
                Assignment: 0.34,
                Read: 0.33,
                Write: 0.33
            }

        statement_type = random.choices(list(statement_probabilities.keys()), list(statement_probabilities.values()))[0]

        return_node = None

        if statement_type == Assignment:
            return_node = Assignment(Identifier(self.generate_new_identifier()), self.generate_expression())
        elif statement_type == Loop:
            return_node = Loop(self.generate_expression(), self.generate_statements())
        elif statement_type == Conditional:
            return_node = Conditional(self.generate_expression(), self.generate_statements())
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


class GP:

    NO_IDENTIFIERS = 3
    MAX_GENERATIONS = 100
    POPULATION_SIZE = 5000
    CROSSOVER_PROBABILITY = 0.6
    MUTATION_PROBABILITY = 0.1
    TOURNAMENT_SIZE = 3
    mutation_count = 0

    def crossover(self, p_1, p_2):
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
                # print('Crossover failed')
                return p_1_copy

        # print('Crossover of {} and {}'.format(random_node_1, random_node_2))

        # Swap the nodes
        node_1_pos = node_1_parent.children.index(random_node_1)
        node_2_pos = node_2_parent.children.index(random_node_2)

        node_1_parent.children[node_1_pos] = random_node_2
        node_2_parent.children[node_2_pos] = random_node_1

        return random.choice([p_1_copy, p_2_copy])

    def mutate(self, program):
        program_copy = deepcopy(program)
        node_to_mutate = random.choice(program_copy.children)
        node_to_mutate_parent = program_copy

        to_mutate = False

        while True:
            mutation_chance = random.random()
            if mutation_chance < self.MUTATION_PROBABILITY:
                to_mutate = True
                break
            if not hasattr(node_to_mutate, 'children') or len(node_to_mutate.children) == 0:
                break
            node_to_mutate_parent = node_to_mutate
            node_to_mutate = random.choice(node_to_mutate.children)

        if not to_mutate:
            return program_copy

        self.mutation_count += 1

        while random.random() > self.MUTATION_PROBABILITY:
            if not hasattr(node_to_mutate, 'children') or len(node_to_mutate.children) == 0:
                break
            node_to_mutate_parent = node_to_mutate
            node_to_mutate = random.choice(node_to_mutate.children)

        node_to_mutate_index = node_to_mutate_parent.children.index(node_to_mutate)
        pg = ProgramGenerator(self.identifiers)

        # print('Mutating {}'.format(node_to_mutate))
        if type(node_to_mutate) == Assignment:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Assignment(Identifier(pg.generate_new_identifier()), pg.generate_expression()))
        elif type(node_to_mutate) == Loop:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Loop(pg.generate_expression(), pg.generate_statements()))
        elif type(node_to_mutate) == Conditional:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Conditional(pg.generate_expression(), pg.generate_statements()))
        elif type(node_to_mutate) == Read:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Read(Identifier(pg.generate_new_identifier())))
        elif type(node_to_mutate) == Write:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Write(pg.generate_expression()))
        elif type(node_to_mutate) == Identifier:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Identifier(pg.generate_identifier()))
        elif type(node_to_mutate) == Literal:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                Literal(str(random.randint(-100, 100))))
        elif type(node_to_mutate) == BinaryOperation:
            match node_to_mutate.name:
                case "||":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_and_expression(), pg.generate_and_expression(), "||"))
                case "&&":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_equality_expression(), pg.generate_equality_expression(), "&&"))
                case "==":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_relational_expression(), pg.generate_relational_expression(),
                                        random.choice(["==", "!="])))
                case "!=":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_relational_expression(), pg.generate_relational_expression(),
                                        random.choice(["==", "!="])))
                case "<":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_additive_expression(), pg.generate_additive_expression(),
                                        random.choice([">=", "<", ">", "<="])))
                case "<=":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_additive_expression(), pg.generate_additive_expression(),
                                        random.choice([">=", "<", ">", "<="])))
                case ">":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_additive_expression(), pg.generate_additive_expression(),
                                        random.choice([">=", "<", ">", "<="])))
                case ">=":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_additive_expression(), pg.generate_additive_expression(),
                                        random.choice([">=", "<", ">", "<="])))
                case "+":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_multiplicative_expression(), pg.generate_multiplicative_expression(),
                                        random.choice(["+", "-"])))
                case "-":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_multiplicative_expression(), pg.generate_multiplicative_expression(),
                                        random.choice(["+", "-"])))
                case "*":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_primary_expression(), pg.generate_primary_expression(),
                                        random.choice(["/", "*"])))
                case "/":
                    node_to_mutate_parent.children[node_to_mutate_index] = (
                        BinaryOperation(pg.generate_primary_expression(), pg.generate_primary_expression(),
                                        random.choice(["/", "*"])))
        elif type(node_to_mutate) == ParenExpression:
            node_to_mutate_parent.children[node_to_mutate_index] = (
                ParenExpression(pg.generate_expression()))

        return program_copy

    def create_population(self):
        pg = ProgramGenerator(self.identifiers)
        return [pg.generate_program() for _ in range(GP.POPULATION_SIZE)]

    def setup_identifiers(self):
        return ['i_' + str(i) for i in range(self.NO_IDENTIFIERS)]

    def stats(self, generation: int):
        # Calculate fitness for each program
        for i in range(self.POPULATION_SIZE):
            self.fitness_table[i] = self.evaluate(self.population[i])

        print('--' * 10)
        print(f'Generation {generation}')
        print(f'Best fitness: {np.min(self.fitness_table)}')
        print(f'Average fitness: {np.average(self.fitness_table)}')
        print(f'Worst fitness: {np.max(self.fitness_table)}')
        print('--' * 10)
        print(f'Best program: {self.population[np.argmin(self.fitness_table)]}')
        print('--' * 10 + '\n')

        self.best_fitness = np.min(self.fitness_table)
        self.best_program = self.population[np.argmin(self.fitness_table)]

    def evaluate(self, program):
        program_code = str(program)
        lexer = SPLexer(InputStream(program_code))
        stream = CommonTokenStream(lexer)
        parser = SPParser(stream)
        tree = parser.program()

        with open('mini_lang/in.in', 'w+') as f:
            random_numbers = [random.random() * 1000 for _ in range(2)]
            f.write('\n'.join([str(random_number) for random_number in random_numbers]))

        visitor = InterpreterVisitor('mini_lang/in.in', 'mini_lang/out.out')

        with open('mini_lang/out.out', 'w') as f:
            f.write('')

        try:
            # print(f'Evaluating program: {program_code}')
            visitor.visit(tree)
        except:
            return 10000000

        del visitor

        return Metric.evaluate_using_metric(MetricType.ANY_POSITION_31415)

    def evolve(self):
        generation = 0
        self.stats(generation)

        while generation < self.MAX_GENERATIONS:
            generation += 1
            if self.best_fitness < 0.00001:
                break
            for _ in range(self.POPULATION_SIZE):
                if random.random() < self.CROSSOVER_PROBABILITY:
                    parent_1_index = self.tournament(self.TOURNAMENT_SIZE)
                    parent_2_index = self.tournament(self.TOURNAMENT_SIZE)
                    new_individual = self.crossover(self.population[parent_1_index], self.population[parent_2_index])
                else:
                    parent_index = self.tournament(self.TOURNAMENT_SIZE)
                    new_individual = self.mutate(self.population[parent_index])

                new_fitness = self.evaluate(new_individual)
                offspring = self.negative_tournament(self.TOURNAMENT_SIZE)
                self.population[offspring] = new_individual
                self.fitness_table[offspring] = new_fitness
            self.mutation_count = 0
            self.stats(generation)

    def negative_tournament(self, tournament_size: int):
        indices = random.sample(range(self.POPULATION_SIZE), tournament_size)
        return indices[np.argmax(self.fitness_table[indices])]

    def tournament(self, tournament_size: int):
        indices = random.sample(range(self.POPULATION_SIZE), tournament_size)
        return indices[np.argmin(self.fitness_table[indices])]

    def __init__(self, seed: int = 0):
        self.fitness_table = np.zeros(self.POPULATION_SIZE)
        self.seed = seed
        if self.seed > 0:
            random.seed(seed)

        self.identifiers = self.setup_identifiers()

        self.best_fitness = 0
        self.best_program = None
        self.population = self.create_population()

        print(self.identifiers)


def main():
    gp = GP()
    gp.evolve()


if __name__ == '__main__':
    main()