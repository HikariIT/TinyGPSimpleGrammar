from antlr4 import FileStream, CommonTokenStream
from gen.SPLexer import SPLexer
from gen.SPParser import SPParser
from visitor import InterpreterVisitor

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    in_file = FileStream('mini_lang/code.test')
    lexer = SPLexer(in_file)
    stream = CommonTokenStream(lexer)
    parser = SPParser(stream)
    tree = parser.program()

    visitor = InterpreterVisitor('mini_lang/in.in', 'mini_lang/out.out')
    visitor.visit(tree)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
