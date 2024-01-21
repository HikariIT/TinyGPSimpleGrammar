from typing import Any


class Variable:
    value: Any
    identifier: str

    def __init__(self, identifier: str):
        self.identifier = identifier
        self.value = None

    def on_assign(self, value: Any):
        self.value = value

    @staticmethod
    def create_and_assign(identifier: str, value: Any) -> "Variable":
        variable = Variable(identifier)
        variable.on_assign(value)
        return variable
