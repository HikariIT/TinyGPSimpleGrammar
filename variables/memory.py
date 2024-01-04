from exceptions import VariableNotDeclaredError, VariableAlreadyDeclaredError
from variables.variable import Variable
from typing import Any
from utils.logger import createLogger
import logging


class VariableMemory:
    variables: dict[str, Variable]
    operation_count: int
    MAX_OPERATIONS: int = 100

    def __init__(self):
        self.variables = {}
        self.operation_count = 0
        self.logger = createLogger("VariableMemory", logging.DEBUG)
        self.logger.info("Variable Memory initialized")

    def __del__(self):
        self.logger.info("Variable Memory deleting")
        self.logger.debug("-" * 30)
        self.logger.debug("Variable storage at end of program:")
        for variable in self.variables.values():
            self.logger.debug(f"{variable.identifier} = {variable.value}")

    def assign_variable(self, identifier: str, value: Any):
        self.operation_count += 1
        if self.operation_count > self.MAX_OPERATIONS:
            raise RecursionError("Too many operations")
        if identifier not in self.variables:
            self.variables[identifier] = Variable(identifier)
        self.logger.debug(f"Assignment: {identifier} <- {value}")
        self.variables[identifier].on_assign(value)

    def get_variable_value(self, identifier: str) -> Any:
        self.operation_count += 1
        if self.operation_count > self.MAX_OPERATIONS:
            raise RecursionError("Too many operations")
        if identifier not in self.variables:
            raise VariableNotDeclaredError(identifier)
        self.logger.debug(f"Get value: {identifier} -> {self.variables[identifier].value}")
        return self.variables[identifier].value

    def is_variable_declared(self, identifier):
        return identifier in self.variables
