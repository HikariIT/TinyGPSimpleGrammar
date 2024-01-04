class VariableNotDeclaredError(Exception):
    def __init__(self, identifier: str):
        super().__init__(f"Variable {identifier} not declared")


class VariableAlreadyDeclaredError(Exception):
    def __init__(self, identifier: str):
        super().__init__(f"Variable {identifier} already declared")
