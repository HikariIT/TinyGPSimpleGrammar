parser grammar SPParser;
options {tokenVocab=SPLexer;}

program     : statementList EOF;

block       : LBRACE statementList RBRACE;

statementList:
            | statement statementList
            | statement;

statement   : assignmentStatement SEMI
            | loopStatement
            | ifStatement
            | read
            | write
            | block
            ;

// Statements ----------------------------------------------------------------------------------------------------------

assignmentStatement
            : identifier ASSIGN expression;

ifStatement : KW_IF LPAREN expression RPAREN statement (KW_ELSE statement)?;

loopStatement
            : KW_WHILE LPAREN expression RPAREN statement;

read        : KW_READ LPAREN identifier RPAREN SEMI;

write       : KW_WRITE LPAREN expression RPAREN SEMI;


// Expressions ---------------------------------------------------------------------------------------------------------

primaryExpression
            : literal
            | identifier
            | castExpression
            | LPAREN expression RPAREN
            ;

unaryExpression
            : unaryOperator primaryExpression
            | primaryExpression;

multiplicativeExpression
            : unaryExpression ((TIMES | DIV) unaryExpression)*
            ;

additiveExpression
            : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
            ;

relationalExpression
            : additiveExpression (relation additiveExpression)?
            ;

equalityExpression
            : relationalExpression (equalityRelation relationalExpression)?
            ;

logicalAndExpression
            : equalityExpression (AND equalityExpression)?
            ;

logicalOrExpression
            : logicalAndExpression (OR logicalAndExpression)?
            ;

expression  : logicalOrExpression;

castExpression
            : typeSpecifier LPAREN expression RPAREN;

// Terminating rules ---------------------------------------------------------------------------------------------------

relation    : LT | LE | GT | GE;

equalityRelation
            : EQ | NE;

unaryOperator
            : PLUS | MINUS | NOT;

literal     : INTEGER_LITERAL
            | FLOAT_LITERAL
            ;

identifier  : IDENTIFIER;

typeSpecifier
            : KW_INT
            | KW_FLOAT
            ;

