# Generated from C:/Users/hikar/Desktop/New programming/RnD/SimplerGrammar/grammar\SPLexer.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,33,183,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,4,12,95,8,12,
        11,12,12,12,96,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,24,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,
        1,29,1,30,4,30,163,8,30,11,30,12,30,164,1,30,5,30,168,8,30,10,30,
        12,30,171,9,30,1,31,4,31,174,8,31,11,31,12,31,175,1,31,1,31,1,32,
        1,32,1,33,1,33,0,0,34,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,65,33,67,0,1,0,4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,
        97,122,3,0,9,10,13,13,32,32,1,0,48,57,185,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,
        0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,
        0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,
        0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,
        0,65,1,0,0,0,1,69,1,0,0,0,3,71,1,0,0,0,5,73,1,0,0,0,7,75,1,0,0,0,
        9,77,1,0,0,0,11,79,1,0,0,0,13,81,1,0,0,0,15,83,1,0,0,0,17,85,1,0,
        0,0,19,87,1,0,0,0,21,89,1,0,0,0,23,91,1,0,0,0,25,94,1,0,0,0,27,98,
        1,0,0,0,29,102,1,0,0,0,31,105,1,0,0,0,33,110,1,0,0,0,35,116,1,0,
        0,0,37,121,1,0,0,0,39,127,1,0,0,0,41,130,1,0,0,0,43,133,1,0,0,0,
        45,137,1,0,0,0,47,143,1,0,0,0,49,146,1,0,0,0,51,149,1,0,0,0,53,151,
        1,0,0,0,55,153,1,0,0,0,57,156,1,0,0,0,59,159,1,0,0,0,61,162,1,0,
        0,0,63,173,1,0,0,0,65,179,1,0,0,0,67,181,1,0,0,0,69,70,5,44,0,0,
        70,2,1,0,0,0,71,72,5,46,0,0,72,4,1,0,0,0,73,74,5,40,0,0,74,6,1,0,
        0,0,75,76,5,41,0,0,76,8,1,0,0,0,77,78,5,123,0,0,78,10,1,0,0,0,79,
        80,5,125,0,0,80,12,1,0,0,0,81,82,5,43,0,0,82,14,1,0,0,0,83,84,5,
        45,0,0,84,16,1,0,0,0,85,86,5,42,0,0,86,18,1,0,0,0,87,88,5,47,0,0,
        88,20,1,0,0,0,89,90,5,61,0,0,90,22,1,0,0,0,91,92,5,59,0,0,92,24,
        1,0,0,0,93,95,3,67,33,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,
        0,96,97,1,0,0,0,97,26,1,0,0,0,98,99,3,25,12,0,99,100,3,3,1,0,100,
        101,3,25,12,0,101,28,1,0,0,0,102,103,5,105,0,0,103,104,5,102,0,0,
        104,30,1,0,0,0,105,106,5,101,0,0,106,107,5,108,0,0,107,108,5,115,
        0,0,108,109,5,101,0,0,109,32,1,0,0,0,110,111,5,119,0,0,111,112,5,
        104,0,0,112,113,5,105,0,0,113,114,5,108,0,0,114,115,5,101,0,0,115,
        34,1,0,0,0,116,117,5,114,0,0,117,118,5,101,0,0,118,119,5,97,0,0,
        119,120,5,100,0,0,120,36,1,0,0,0,121,122,5,119,0,0,122,123,5,114,
        0,0,123,124,5,105,0,0,124,125,5,116,0,0,125,126,5,101,0,0,126,38,
        1,0,0,0,127,128,5,38,0,0,128,129,5,38,0,0,129,40,1,0,0,0,130,131,
        5,124,0,0,131,132,5,124,0,0,132,42,1,0,0,0,133,134,5,105,0,0,134,
        135,5,110,0,0,135,136,5,116,0,0,136,44,1,0,0,0,137,138,5,102,0,0,
        138,139,5,108,0,0,139,140,5,111,0,0,140,141,5,97,0,0,141,142,5,116,
        0,0,142,46,1,0,0,0,143,144,5,61,0,0,144,145,5,61,0,0,145,48,1,0,
        0,0,146,147,5,33,0,0,147,148,5,61,0,0,148,50,1,0,0,0,149,150,5,60,
        0,0,150,52,1,0,0,0,151,152,5,62,0,0,152,54,1,0,0,0,153,154,5,60,
        0,0,154,155,5,61,0,0,155,56,1,0,0,0,156,157,5,62,0,0,157,158,5,61,
        0,0,158,58,1,0,0,0,159,160,5,33,0,0,160,60,1,0,0,0,161,163,7,0,0,
        0,162,161,1,0,0,0,163,164,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,
        0,165,169,1,0,0,0,166,168,7,1,0,0,167,166,1,0,0,0,168,171,1,0,0,
        0,169,167,1,0,0,0,169,170,1,0,0,0,170,62,1,0,0,0,171,169,1,0,0,0,
        172,174,7,2,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,
        175,176,1,0,0,0,176,177,1,0,0,0,177,178,6,31,0,0,178,64,1,0,0,0,
        179,180,7,3,0,0,180,66,1,0,0,0,181,182,7,3,0,0,182,68,1,0,0,0,5,
        0,96,164,169,175,1,6,0,0
    ]

class SPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMA = 1
    DOT = 2
    LPAREN = 3
    RPAREN = 4
    LBRACE = 5
    RBRACE = 6
    PLUS = 7
    MINUS = 8
    TIMES = 9
    DIV = 10
    ASSIGN = 11
    SEMI = 12
    INTEGER_LITERAL = 13
    FLOAT_LITERAL = 14
    KW_IF = 15
    KW_ELSE = 16
    KW_WHILE = 17
    KW_READ = 18
    KW_WRITE = 19
    AND = 20
    OR = 21
    KW_INT = 22
    KW_FLOAT = 23
    EQ = 24
    NE = 25
    LT = 26
    GT = 27
    LE = 28
    GE = 29
    NOT = 30
    IDENTIFIER = 31
    WS = 32
    DIGIT = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'.'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
            "'/'", "'='", "';'", "'if'", "'else'", "'while'", "'read'", 
            "'write'", "'&&'", "'||'", "'int'", "'float'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", 
            "MINUS", "TIMES", "DIV", "ASSIGN", "SEMI", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "KW_IF", "KW_ELSE", "KW_WHILE", "KW_READ", 
            "KW_WRITE", "AND", "OR", "KW_INT", "KW_FLOAT", "EQ", "NE", "LT", 
            "GT", "LE", "GE", "NOT", "IDENTIFIER", "WS", "DIGIT" ]

    ruleNames = [ "COMMA", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "PLUS", "MINUS", "TIMES", "DIV", "ASSIGN", "SEMI", "INTEGER_LITERAL", 
                  "FLOAT_LITERAL", "KW_IF", "KW_ELSE", "KW_WHILE", "KW_READ", 
                  "KW_WRITE", "AND", "OR", "KW_INT", "KW_FLOAT", "EQ", "NE", 
                  "LT", "GT", "LE", "GE", "NOT", "IDENTIFIER", "WS", "DIGIT", 
                  "DEC_DIGIT" ]

    grammarFileName = "SPLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


