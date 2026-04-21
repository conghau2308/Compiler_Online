grammar CS;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// --- PARSER --- //

// TODO Literal Integer, floating-point, and string literals


// TODO Expressions
/*
| **Operator** | **Associativity** |
|--------------|-------------------|
| `.` (member access) | left |
| `++`, `--` (postfix) | left |
| `++`, `--` (prefix) | right |
| `!`, `-` (unary), `+` (unary) | right |
| `*`, `/`, `%` | left |
| `+`, `-` (binary) | left |
| `<`, `<=`, `>`, `>=` | left |
| `==`, `!=` | left |
| `&&` | left |
| `\|\|` | left |
| `=` | right |
Primary expressions (identifiers, literals, parenthesized, member access), 
unary operations, binary operations following operator precedence, 
function calls, and postfix operations (increment/decrement)
*/
list_expression: expression (COMMA expression)*;
expression: lhs ASSIGN expression | expression1;
expression1: expression2 (OR expression2)*;
expression2: expression3 (AND expression3)*;
expression3: expression4 ((EQ | NEQ) expression4)*;
expression4: expression5 ((LT | LTE | GT | GTE) expression5)*;
expression5: expression6 ((PLUS | SUB) expression6)*;
expression6: expression7 ((MUL | DIV | MOD) expression7)*;
expression7: (NOT | SUB | PLUS) expression7 | expression8;
expression8: (INCRE | DECRE) expression8 | expression9;
expression9: expression10 (INCRE | DECRE)*;
expression10: expression10 ACCESS ID | expression11;
expression11: literal | struct_literal | function_call | ID | LPAREN expression RPAREN;
function_call: ID LPAREN list_expression? RPAREN;
lhs: expression10 ACCESS ID | ID;

literal: INT_LIT | FLOAT_LIT | STRING_LIT;
struct_literal: LBRACE list_expression? RBRACE;


// TODO type `int`, `float`, `string`, `void`, struct types, and type inference using `auto`
all_type: primitive_type | ID | AUTO;
primitive_type: INT | FLOAT | STRING | VOID;
var_type: INT | FLOAT | STRING | ID | AUTO;
function_type: primitive_type | ID;

// TODO Statements Variable declarations, assignments, control flow (if, while, for, switch-case), break, continue, return, expression statements, and blocks
list_statement: statement+;
statement: var_statement SEMI
		| if_statement
		| while_statement
		| for_statement
        | switch_statement
		| break_statement
		| continue_statement
        | block_statement
        | expression_statement
		| return_statement;
var_statement: var_type ID (ASSIGN init_value)?;
init_value: expression | struct_literal;
block_statement: LBRACE statement* RBRACE;
if_statement: IF LPAREN expression RPAREN statement (ELSE statement)?;
while_statement: WHILE LPAREN expression RPAREN statement;
for_statement: FOR LPAREN for_init? SEMI expression? SEMI for_update? RPAREN statement;
for_init: var_statement | assign_init;
assign_init: lhs ASSIGN expression;
for_update: lhs ASSIGN expression | (INCRE | DECRE) expression8 | expression10 (INCRE | DECRE)+;
switch_statement: SWITCH LPAREN expression RPAREN LBRACE case_section* default_section? case_section* RBRACE;
case_section: CASE expression COLON statement*;
default_section: DEFAULT COLON statement*;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
expression_statement: expression SEMI;
return_statement: RETURN init_value? SEMI;

// TODO Structs and Functions
program: (structs | functions)* EOF;
structs: STRUCT ID LBRACE struct_body* RBRACE SEMI;
struct_body: explicit_type ID SEMI;
explicit_type: (INT | FLOAT | STRING | ID);
functions: function_type? ID LPAREN list_parameter? RPAREN block_statement;
list_parameter: parameter (COMMA parameter)*;
parameter: explicit_type ID;


// --- TODO TASK LEXER --- //
// TODO Keywords
AUTO     : 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';

STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// TODO Operator
// int or float
PLUS        : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';

EQ          : '==';
NEQ         : '!=';
LT          : '<';
GT          : '>';
LTE         : '<=';
GTE         : '>=';

// int only
MOD         : '%';

OR          : '||';
AND         : '&&';
NOT         : '!';
INCRE       : '++';
DECRE       : '--';

// any
ASSIGN      : '=';

// struct
ACCESS      : '.';

// TODO Separator
LBRACE   : '{';
RBRACE   : '}';
LPAREN   : '(';
RPAREN   : ')';
SEMI     : ';';
COMMA    : ',';
COLON    : ':';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literals
INT_LIT: [0-9]+;

FLOAT_LIT: DIGITS '.' DIGITS? EXP? | '.' DIGITS EXP? | DIGITS EXP;
fragment DIGITS: [0-9]+;
fragment EXP: [Ee][+-]?[0-9]+;

STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ~[\r\n\\"] | ECS_SEQ;
fragment ECS_SEQ: '\\' [bfrnt"\\];
fragment ESC_ILLEGAL: '\\' ~[bfrnt"\\];

// TODO Comment and WS
WS: [ \t\r\n\f]+ -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// TODO ERROR
UNCLOSE_STRING: '"' STR_CHAR*  '\\'? ('\n' | '\r\n' | EOF) {
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL { raise IllegalEscape(self.text[1:]) };
ERROR_CHAR: .;
