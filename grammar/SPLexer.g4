lexer grammar SPLexer;

COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

// Operations
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';

// Assignment operators
ASSIGN: '=';
SEMI: ';';

// Literals
INTEGER_LITERAL : DEC_DIGIT+;
FLOAT_LITERAL   : INTEGER_LITERAL DOT INTEGER_LITERAL;

// Keywords
KW_IF: 'if';
KW_ELSE: 'else';
KW_WHILE: 'while';
KW_READ: 'read';
KW_WRITE: 'write';

// Logical operators
AND: '&&';
OR: '||';

// Types
KW_INT: 'int';
KW_FLOAT: 'float';

// Relations
EQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
NOT: '!';

IDENTIFIER
    : [A-Za-z_]+ [A-Za-z_0-9]*
    ;
WS          : [ \t\r\n]+ -> skip;
DIGIT       : [0-9];

fragment DEC_DIGIT: [0-9];