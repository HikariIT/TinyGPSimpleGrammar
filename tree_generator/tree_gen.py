import json
import random


class TerminalNodeGenerator:
    def __init__(self, no_identifiers: int):
        self.no_identifiers = no_identifiers
        self.identifiers = [f"i_{i}" for i in range(no_identifiers)]
        self.int_bounds = (-100, 100)
        self.float_bounds = (-100, 100)

    def get_random_identifier(self):
        return random.choice(self.identifiers)

    def get_random_int_literal(self):
        return random.randint(self.int_bounds[0], self.int_bounds[1])

    def get_random_float_literal(self):
        return random.uniform(self.float_bounds[0], self.float_bounds[1])


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
            print(x.name)

    elif is_last:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.name)
        flag[depth] = False

    else:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.name)

    if type(x) != Node:
        return

    it = 0
    for i in x.children:
        it += 1
        print_tree(i, flag, depth + 1, it == (len(x.children) - 1))
    flag[depth] = True


class Node:

    def __init__(self, name: str):
        self.children = []
        self.name = name
        self.selected_rule = -1
        self.no_rules = 0


class Generator:

    max_depth = 5
    TERMINALS = {
        'COMMA': ',',
        'DOT': '.',
        'LPAREN': '(',
        'RPAREN': ')',
        'LBRACE': '{',
        'RBRACE': '}',
        'PLUS': '+',
        'MINUS': '-',
        'TIMES': '*',
        'DIV': '/',
        'ASSIGN': '=',
        'SEMI': ';',
        'KW_IF': 'if',
        'KW_ELSE': 'else',
        'KW_WHILE': 'while',
        'KW_READ': 'read',
        'KW_WRITE': 'write',
        'AND': '&&',
        'OR': '||',
        'KW_INT': 'int',
        'KW_FLOAT': 'float',
        'EQ': '==',
        'NE': '!=',
        'LT': '<',
        'GT': '>',
        'LE': '<=',
        'GE': '>=',
        'NOT': '!',
    }

    def __init__(self, no_identifiers: int, max_depth: int, starting_node: Node = None):
        self.terminal_node_generator = TerminalNodeGenerator(no_identifiers)
        self.depth = 0
        self.max_depth = max_depth

        with open('tree_generator/rules.json') as json_file:
            self.rules = json.load(json_file)
            for node, rules in self.rules.items():
                self.rules[node] = list(rules.values())

        self.root = starting_node if starting_node else Node('program')
        self.unterminated_nodes = []
        self.process_node(self.root)
        if len(self.unterminated_nodes) > 0:
            print(f"WARNING: Unterminated nodes: {[node.name for node in self.unterminated_nodes]}")
        # self.walk_node(self.root)

    def get_tree(self):
        return self.root

    def process_node(self, node: Node | str, exclude_option: int = -1):
        self.depth += 1

        if type(node) == Node:
            self.unterminated_nodes.append(node)
        else:
            self.depth -= 1
            return

        if self.depth > self.max_depth:
            return

        node_name = node.name
        rules = self.rules[node_name]

        probabilities = [rule[-1] for rule in rules]
        rules = [rule[:-1] for rule in rules]

        # Random choice based on probabilities
        cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
        random_number = random.random()

        if exclude_option != -1:
            rule_id = -1
            while rule_id == exclude_option:
                for i, cumulative_probability in enumerate(cumulative_probabilities):
                    if random_number <= cumulative_probability:
                        rule_id = i
                        break
            rule = rules[rule_id]

        else:
            rule = []
            for i, cumulative_probability in enumerate(cumulative_probabilities):
                if random_number <= cumulative_probability:
                    rule = rules[i]
                    node.selected_rule = i
                    node.no_rules = len(rules)
                    break

        # Iterate over children of rule
        for child in rule:
            if child == 'IDENTIFIER':
                child = self.terminal_node_generator.get_random_identifier()
                node.children.append(child)
            elif child == 'INTEGER_LITERAL':
                child = self.terminal_node_generator.get_random_int_literal()
                node.children.append(child)
            elif child == 'FLOAT_LITERAL':
                child = self.terminal_node_generator.get_random_float_literal()
                node.children.append(child)
            elif child in self.TERMINALS:
                node.children.append(self.TERMINALS[child])
            else:
                node.children.append(Node(child))
                self.process_node(node.children[-1])

        if not any([child in self.unterminated_nodes for child in node.children]):
            self.unterminated_nodes.remove(node)

        self.depth -= 1

    @staticmethod
    def walk_node(node: Node | str):
        if type(node) != Node:
            if node == ';':
                print(node)
            else:
                print(node, end=' ')
        else:
            for child in node.children:
                Generator.walk_node(child)


