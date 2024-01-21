import math
from enum import Enum


class MetricType(Enum):
    ANY_POSITION_1 = 1
    ANY_POSITION_789 = 2
    ANY_POSITION_31415 = 3
    FIRST_POSITION_1 = 4
    FIRST_POSITION_789 = 5
    ONLY_1 = 6
    SUM_OF_TWO = 7
    SMALL_OR_LARGE = 8
    SUM_OF_SQUARES = 9
    MULTIPLY_TWO = 10
    ONLY_31435 = 11


class Metric:

    @staticmethod
    def evaluate_using_metric(metric_type: MetricType):
        match metric_type:
            case MetricType.ANY_POSITION_1:
                return Metric.any_position_1()
            case MetricType.ANY_POSITION_789:
                return Metric.any_position_789()
            case MetricType.ANY_POSITION_31415:
                return Metric.any_position_31415()
            case MetricType.FIRST_POSITION_1:
                return Metric.first_position_1()
            case MetricType.FIRST_POSITION_789:
                return Metric.first_position_789()
            case MetricType.ONLY_1:
                return Metric.only_1()
            case MetricType.SUM_OF_TWO:
                return Metric.sum_of_two()
            case MetricType.SMALL_OR_LARGE:
                return Metric.small_or_large()
            case MetricType.SUM_OF_SQUARES:
                return Metric.sum_of_squares()
            case MetricType.MULTIPLY_TWO:
                return Metric.multiply_two()
            case MetricType.ONLY_31435:
                return Metric.only_31435()
            case _:
                raise Exception("Invalid metric type")

    @staticmethod
    def get_output_from_program() -> str:
        with open('mini_lang/out.out', 'r') as f:
            return f.read()

    @staticmethod
    def any_position_1() -> float:
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 1:
                    return 0
            except ValueError:
                pass

        if len(lines) == 0:
            return 1000

        return 10

    @staticmethod
    def any_position_789():
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 789:
                    return 0
            except ValueError:
                pass

        if len(lines) == 0:
            return 1000

        return 10

    @staticmethod
    def any_position_31415():
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 31415:
                    return 0
                return min(abs(31415 - line_value), 50000)
            except ValueError:
                pass

        if len(lines) == 0:
            return 1000000

        return 100000

    @staticmethod
    def first_position_1():
        return 4

    @staticmethod
    def first_position_789():
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()
        if len(lines) == 0:
            return 1000
        if len(lines) > 1:
            return 2000

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 789:
                    return 0
            except ValueError:
                pass

        return 10

    @staticmethod
    def only_1():
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()
        if len(lines) == 0:
            return 1000
        if len(lines) > 1:
            return 2000

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 1:
                    return 0
            except ValueError:
                pass

        return 10

    @staticmethod
    def only_31435():
        output = Metric.get_output_from_program()
        # print(f'Output: {output}')
        lines = output.splitlines()
        if len(lines) == 0:
            return 1000
        if len(lines) > 1:
            return 2000

        for line in lines:
            try:
                line_value = float(line)
                if line_value == 31435:
                    return 0
                elif 0 < line_value < 2*31415:
                    return abs(31415 - line_value)/31415*100
            except ValueError:
                pass

        return 100

    @staticmethod
    def sum_of_two():
        program_input = Metric.get_input_of_program()
        num_1 = float(program_input.splitlines()[0])
        num_2 = float(program_input.splitlines()[1])

        sum_of_two = num_1 + num_2

        output = Metric.get_output_from_program()

        if len(output.splitlines()) == 0:
            return 2000

        if len(output.splitlines()) > 1:
            return 1000

        try:
            output_value = float(output)
            if math.isclose(output_value, sum_of_two):
                return 0
            return 10
        except ValueError:
            return 1000

    @staticmethod
    def multiply_two():
        program_input = Metric.get_input_of_program()
        num_1 = float(program_input.splitlines()[0])
        num_2 = float(program_input.splitlines()[1])

        sum_of_two = num_1 * num_2

        output = Metric.get_output_from_program()

        if len(output.splitlines()) == 0:
            return 2000

        if len(output.splitlines()) > 1:
            return 1000

        try:
            output_value = float(output)
            if math.isclose(output_value, sum_of_two):
                return 0
            return 10
        except ValueError:
            return 1000

    @staticmethod
    def small_or_large():
        program_input = Metric.get_input_of_program()
        num_1 = float(program_input.splitlines()[0])
        output = Metric.get_output_from_program()

        if len(output.splitlines()) == 0:
            return 2000

        if len(output.splitlines()) > 1:
            return 1000

        try:
            output_value = float(output)
            if num_1 < 1000 and math.isclose(-1, output_value):
                return 0
            if num_1 > 2000 and math.isclose(1, output_value):
                return 0
            return 10
        except ValueError:
            return 1000

    @staticmethod
    def sum_of_squares():
        program_input = Metric.get_input_of_program()
        num_1 = float(program_input.splitlines()[0])
        num_2 = float(program_input.splitlines()[1])

        sum_of_squares = num_1 ** 2 + num_2 ** 2

        output = Metric.get_output_from_program()

        if len(output.splitlines()) == 0:
            return 2000

        if len(output.splitlines()) > 1:
            return 1000

        try:
            output_value = float(output)
            if math.isclose(output_value, sum_of_squares):
                return 0
            return 10
        except ValueError:
            return 1000

    @staticmethod
    def get_input_of_program() -> str:
        with open('mini_lang/in.in', 'r') as f:
            return f.read()
