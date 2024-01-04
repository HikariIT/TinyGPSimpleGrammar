# Generated from C:/Users/hikar/Desktop/New programming/RnD/SimplerGrammar/grammar\SPParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,73,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        86,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,113,8,9,1,10,1,10,
        1,10,1,10,3,10,119,8,10,1,11,1,11,1,11,5,11,124,8,11,10,11,12,11,
        127,9,11,1,12,1,12,1,12,5,12,132,8,12,10,12,12,12,135,9,12,1,13,
        1,13,1,13,1,13,3,13,141,8,13,1,14,1,14,1,14,1,14,3,14,147,8,14,1,
        15,1,15,1,15,3,15,152,8,15,1,16,1,16,1,16,3,16,157,8,16,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,0,7,1,0,9,10,1,0,7,8,1,0,26,
        29,1,0,24,25,2,0,7,8,30,30,1,0,13,14,1,0,22,23,170,0,50,1,0,0,0,
        2,53,1,0,0,0,4,62,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,10,78,1,0,0,
        0,12,87,1,0,0,0,14,93,1,0,0,0,16,99,1,0,0,0,18,112,1,0,0,0,20,118,
        1,0,0,0,22,120,1,0,0,0,24,128,1,0,0,0,26,136,1,0,0,0,28,142,1,0,
        0,0,30,148,1,0,0,0,32,153,1,0,0,0,34,158,1,0,0,0,36,160,1,0,0,0,
        38,165,1,0,0,0,40,167,1,0,0,0,42,169,1,0,0,0,44,171,1,0,0,0,46,173,
        1,0,0,0,48,175,1,0,0,0,50,51,3,4,2,0,51,52,5,0,0,1,52,1,1,0,0,0,
        53,54,5,5,0,0,54,55,3,4,2,0,55,56,5,6,0,0,56,3,1,0,0,0,57,63,1,0,
        0,0,58,59,3,6,3,0,59,60,3,4,2,0,60,63,1,0,0,0,61,63,3,6,3,0,62,57,
        1,0,0,0,62,58,1,0,0,0,62,61,1,0,0,0,63,5,1,0,0,0,64,65,3,8,4,0,65,
        66,5,12,0,0,66,73,1,0,0,0,67,73,3,12,6,0,68,73,3,10,5,0,69,73,3,
        14,7,0,70,73,3,16,8,0,71,73,3,2,1,0,72,64,1,0,0,0,72,67,1,0,0,0,
        72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,7,1,0,
        0,0,74,75,3,46,23,0,75,76,5,11,0,0,76,77,3,34,17,0,77,9,1,0,0,0,
        78,79,5,15,0,0,79,80,5,3,0,0,80,81,3,34,17,0,81,82,5,4,0,0,82,85,
        3,6,3,0,83,84,5,16,0,0,84,86,3,6,3,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,11,1,0,0,0,87,88,5,17,0,0,88,89,5,3,0,0,89,90,3,34,17,0,90,91,
        5,4,0,0,91,92,3,6,3,0,92,13,1,0,0,0,93,94,5,18,0,0,94,95,5,3,0,0,
        95,96,3,46,23,0,96,97,5,4,0,0,97,98,5,12,0,0,98,15,1,0,0,0,99,100,
        5,19,0,0,100,101,5,3,0,0,101,102,3,34,17,0,102,103,5,4,0,0,103,104,
        5,12,0,0,104,17,1,0,0,0,105,113,3,44,22,0,106,113,3,46,23,0,107,
        113,3,36,18,0,108,109,5,3,0,0,109,110,3,34,17,0,110,111,5,4,0,0,
        111,113,1,0,0,0,112,105,1,0,0,0,112,106,1,0,0,0,112,107,1,0,0,0,
        112,108,1,0,0,0,113,19,1,0,0,0,114,115,3,42,21,0,115,116,3,18,9,
        0,116,119,1,0,0,0,117,119,3,18,9,0,118,114,1,0,0,0,118,117,1,0,0,
        0,119,21,1,0,0,0,120,125,3,20,10,0,121,122,7,0,0,0,122,124,3,20,
        10,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,
        0,0,126,23,1,0,0,0,127,125,1,0,0,0,128,133,3,22,11,0,129,130,7,1,
        0,0,130,132,3,22,11,0,131,129,1,0,0,0,132,135,1,0,0,0,133,131,1,
        0,0,0,133,134,1,0,0,0,134,25,1,0,0,0,135,133,1,0,0,0,136,140,3,24,
        12,0,137,138,3,38,19,0,138,139,3,24,12,0,139,141,1,0,0,0,140,137,
        1,0,0,0,140,141,1,0,0,0,141,27,1,0,0,0,142,146,3,26,13,0,143,144,
        3,40,20,0,144,145,3,26,13,0,145,147,1,0,0,0,146,143,1,0,0,0,146,
        147,1,0,0,0,147,29,1,0,0,0,148,151,3,28,14,0,149,150,5,20,0,0,150,
        152,3,28,14,0,151,149,1,0,0,0,151,152,1,0,0,0,152,31,1,0,0,0,153,
        156,3,30,15,0,154,155,5,21,0,0,155,157,3,30,15,0,156,154,1,0,0,0,
        156,157,1,0,0,0,157,33,1,0,0,0,158,159,3,32,16,0,159,35,1,0,0,0,
        160,161,3,48,24,0,161,162,5,3,0,0,162,163,3,34,17,0,163,164,5,4,
        0,0,164,37,1,0,0,0,165,166,7,2,0,0,166,39,1,0,0,0,167,168,7,3,0,
        0,168,41,1,0,0,0,169,170,7,4,0,0,170,43,1,0,0,0,171,172,7,5,0,0,
        172,45,1,0,0,0,173,174,5,31,0,0,174,47,1,0,0,0,175,176,7,6,0,0,176,
        49,1,0,0,0,11,62,72,85,112,118,125,133,140,146,151,156
    ]

class SPParser ( Parser ):

    grammarFileName = "SPParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "';'", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'while'", "'read'", 
                     "'write'", "'&&'", "'||'", "'int'", "'float'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "DOT", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "PLUS", "MINUS", "TIMES", "DIV", "ASSIGN", 
                      "SEMI", "INTEGER_LITERAL", "FLOAT_LITERAL", "KW_IF", 
                      "KW_ELSE", "KW_WHILE", "KW_READ", "KW_WRITE", "AND", 
                      "OR", "KW_INT", "KW_FLOAT", "EQ", "NE", "LT", "GT", 
                      "LE", "GE", "NOT", "IDENTIFIER", "WS", "DIGIT" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statementList = 2
    RULE_statement = 3
    RULE_assignmentStatement = 4
    RULE_ifStatement = 5
    RULE_loopStatement = 6
    RULE_read = 7
    RULE_write = 8
    RULE_primaryExpression = 9
    RULE_unaryExpression = 10
    RULE_multiplicativeExpression = 11
    RULE_additiveExpression = 12
    RULE_relationalExpression = 13
    RULE_equalityExpression = 14
    RULE_logicalAndExpression = 15
    RULE_logicalOrExpression = 16
    RULE_expression = 17
    RULE_castExpression = 18
    RULE_relation = 19
    RULE_equalityRelation = 20
    RULE_unaryOperator = 21
    RULE_literal = 22
    RULE_identifier = 23
    RULE_typeSpecifier = 24

    ruleNames =  [ "program", "block", "statementList", "statement", "assignmentStatement", 
                   "ifStatement", "loopStatement", "read", "write", "primaryExpression", 
                   "unaryExpression", "multiplicativeExpression", "additiveExpression", 
                   "relationalExpression", "equalityExpression", "logicalAndExpression", 
                   "logicalOrExpression", "expression", "castExpression", 
                   "relation", "equalityRelation", "unaryOperator", "literal", 
                   "identifier", "typeSpecifier" ]

    EOF = Token.EOF
    COMMA=1
    DOT=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    PLUS=7
    MINUS=8
    TIMES=9
    DIV=10
    ASSIGN=11
    SEMI=12
    INTEGER_LITERAL=13
    FLOAT_LITERAL=14
    KW_IF=15
    KW_ELSE=16
    KW_WHILE=17
    KW_READ=18
    KW_WRITE=19
    AND=20
    OR=21
    KW_INT=22
    KW_FLOAT=23
    EQ=24
    NE=25
    LT=26
    GT=27
    LE=28
    GE=29
    NOT=30
    IDENTIFIER=31
    WS=32
    DIGIT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(SPParser.StatementListContext,0)


        def EOF(self):
            return self.getToken(SPParser.EOF, 0)

        def getRuleIndex(self):
            return SPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.statementList()
            self.state = 51
            self.match(SPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SPParser.LBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(SPParser.StatementListContext,0)


        def RBRACE(self):
            return self.getToken(SPParser.RBRACE, 0)

        def getRuleIndex(self):
            return SPParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SPParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(SPParser.LBRACE)
            self.state = 54
            self.statementList()
            self.state = 55
            self.match(SPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SPParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(SPParser.StatementListContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = SPParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementList)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.statement()
                self.state = 59
                self.statementList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(SPParser.AssignmentStatementContext,0)


        def SEMI(self):
            return self.getToken(SPParser.SEMI, 0)

        def loopStatement(self):
            return self.getTypedRuleContext(SPParser.LoopStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SPParser.IfStatementContext,0)


        def read(self):
            return self.getTypedRuleContext(SPParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(SPParser.WriteContext,0)


        def block(self):
            return self.getTypedRuleContext(SPParser.BlockContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.assignmentStatement()
                self.state = 65
                self.match(SPParser.SEMI)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.loopStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.ifStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.read()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.write()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SPParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(SPParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = SPParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.identifier()
            self.state = 75
            self.match(SPParser.ASSIGN)
            self.state = 76
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(SPParser.KW_IF, 0)

        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.StatementContext)
            else:
                return self.getTypedRuleContext(SPParser.StatementContext,i)


        def KW_ELSE(self):
            return self.getToken(SPParser.KW_ELSE, 0)

        def getRuleIndex(self):
            return SPParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SPParser.KW_IF)
            self.state = 79
            self.match(SPParser.LPAREN)
            self.state = 80
            self.expression()
            self.state = 81
            self.match(SPParser.RPAREN)
            self.state = 82
            self.statement()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 83
                self.match(SPParser.KW_ELSE)
                self.state = 84
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHILE(self):
            return self.getToken(SPParser.KW_WHILE, 0)

        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(SPParser.StatementContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = SPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SPParser.KW_WHILE)
            self.state = 88
            self.match(SPParser.LPAREN)
            self.state = 89
            self.expression()
            self.state = 90
            self.match(SPParser.RPAREN)
            self.state = 91
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_READ(self):
            return self.getToken(SPParser.KW_READ, 0)

        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(SPParser.IdentifierContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(SPParser.SEMI, 0)

        def getRuleIndex(self):
            return SPParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = SPParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(SPParser.KW_READ)
            self.state = 94
            self.match(SPParser.LPAREN)
            self.state = 95
            self.identifier()
            self.state = 96
            self.match(SPParser.RPAREN)
            self.state = 97
            self.match(SPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WRITE(self):
            return self.getToken(SPParser.KW_WRITE, 0)

        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(SPParser.SEMI, 0)

        def getRuleIndex(self):
            return SPParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = SPParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SPParser.KW_WRITE)
            self.state = 100
            self.match(SPParser.LPAREN)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(SPParser.RPAREN)
            self.state = 103
            self.match(SPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SPParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SPParser.IdentifierContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(SPParser.CastExpressionContext,0)


        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def getRuleIndex(self):
            return SPParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = SPParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primaryExpression)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.literal()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.identifier()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.castExpression()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(SPParser.LPAREN)
                self.state = 109
                self.expression()
                self.state = 110
                self.match(SPParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(SPParser.UnaryOperatorContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(SPParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = SPParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unaryExpression)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.unaryOperator()
                self.state = 115
                self.primaryExpression()
                pass
            elif token in [3, 13, 14, 22, 23, 31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.UnaryExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(SPParser.TIMES)
            else:
                return self.getToken(SPParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SPParser.DIV)
            else:
                return self.getToken(SPParser.DIV, i)

        def getRuleIndex(self):
            return SPParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = SPParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.unaryExpression()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.unaryExpression()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SPParser.PLUS)
            else:
                return self.getToken(SPParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SPParser.MINUS)
            else:
                return self.getToken(SPParser.MINUS, i)

        def getRuleIndex(self):
            return SPParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = SPParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.multiplicativeExpression()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 129
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self.multiplicativeExpression()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.AdditiveExpressionContext,i)


        def relation(self):
            return self.getTypedRuleContext(SPParser.RelationContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = SPParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.additiveExpression()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 137
                self.relation()
                self.state = 138
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.RelationalExpressionContext,i)


        def equalityRelation(self):
            return self.getTypedRuleContext(SPParser.EqualityRelationContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = SPParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.relationalExpression()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==25:
                self.state = 143
                self.equalityRelation()
                self.state = 144
                self.relationalExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.EqualityExpressionContext,i)


        def AND(self):
            return self.getToken(SPParser.AND, 0)

        def getRuleIndex(self):
            return SPParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = SPParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.equalityExpression()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 149
                self.match(SPParser.AND)
                self.state = 150
                self.equalityExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(SPParser.LogicalAndExpressionContext,i)


        def OR(self):
            return self.getToken(SPParser.OR, 0)

        def getRuleIndex(self):
            return SPParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = SPParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.logicalAndExpression()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 154
                self.match(SPParser.OR)
                self.state = 155
                self.logicalAndExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(SPParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return SPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(SPParser.TypeSpecifierContext,0)


        def LPAREN(self):
            return self.getToken(SPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SPParser.RPAREN, 0)

        def getRuleIndex(self):
            return SPParser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = SPParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.typeSpecifier()
            self.state = 161
            self.match(SPParser.LPAREN)
            self.state = 162
            self.expression()
            self.state = 163
            self.match(SPParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(SPParser.LT, 0)

        def LE(self):
            return self.getToken(SPParser.LE, 0)

        def GT(self):
            return self.getToken(SPParser.GT, 0)

        def GE(self):
            return self.getToken(SPParser.GE, 0)

        def getRuleIndex(self):
            return SPParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = SPParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SPParser.EQ, 0)

        def NE(self):
            return self.getToken(SPParser.NE, 0)

        def getRuleIndex(self):
            return SPParser.RULE_equalityRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityRelation" ):
                listener.enterEqualityRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityRelation" ):
                listener.exitEqualityRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityRelation" ):
                return visitor.visitEqualityRelation(self)
            else:
                return visitor.visitChildren(self)




    def equalityRelation(self):

        localctx = SPParser.EqualityRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_equalityRelation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(SPParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SPParser.MINUS, 0)

        def NOT(self):
            return self.getToken(SPParser.NOT, 0)

        def getRuleIndex(self):
            return SPParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperator" ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = SPParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742208) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(SPParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(SPParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return SPParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SPParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SPParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SPParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = SPParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(SPParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(SPParser.KW_INT, 0)

        def KW_FLOAT(self):
            return self.getToken(SPParser.KW_FLOAT, 0)

        def getRuleIndex(self):
            return SPParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = SPParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





