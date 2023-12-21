from tree_generator.tree_gen import Generator, Node, print_tree
import random
import json


class GPTest:
    POPULATION_SIZE = 1

    def __init__(self):
        self.population = []
        with open('tree_generator/rules.json') as json_file:
            self.rules = json.load(json_file)
            for node, rules in self.rules.items():
                self.rules[node] = list(rules.values())

        self.leaves = []
        self.generate_population()

    def generate_population(self):
        for i in range(self.POPULATION_SIZE):
            self.population.append(self.get_random_individual())

    @staticmethod
    def get_random_individual():
        return Generator(3, 5).get_tree()

    def select_random_leaf(self, node, current_depth: int):
        if type(node) != Node:
            return
        if current_depth == 5:
            self.leaves.append(node)
        for child in node.children:
            self.select_random_leaf(child, current_depth + 1)

    def grow(self, root: Node):
        print_tree(root, [True] * 100, 0, True)
        Generator.walk_node(root)
        self.leaves = []
        self.select_random_leaf(root, 0)
        if len(self.leaves) == 1:
            node = self.leaves[0]
        else:
            node = random.choice(self.leaves)

        print(f'\nSelected node: {node.name}')

        Generator(3, 2, node)
        print_tree(root, [True] * 100, 0, True)
        Generator.walk_node(root)

    def generation(self):
        pass

    def crossover(self, parent1, parent2):
        pass


gp = GPTest()
gp.grow(gp.population[0])
