import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens


# Placeholder grammar expression reference:
# def p_optitem(p):
#     'optitem : item'
#     '        | empty'

#######################FOR LARGER GRAMMAR SUBSETS###########################
# start = 'foo'
#
# def p_bar(p):
#     'bar : A B'
#
# # This is the starting rule due to the start specifier above
# def p_foo(p):
#     'foo : bar X'
#######################FOR LARGER GRAMMAR SUBSETS###########################


#######################p.value ASSINGNING SAMPLE############################
# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     #   ^            ^        ^    ^
#     #  p[0]         p[1]     p[2] p[3]
#
#     p[0] = p[1] + p[3]
#######################p.value ASSINGNING SAMPLE############################

def SpeedFunc(p): #Defined what speed is
    'SpeedFunc : SPEED EQUALS NUMBERS'
    print(type)
    p[0] = p[3]

def GravityFunc(p): #Defined what gravity is
    'GravityFunc : GRAVITY EQUALS NUMBERS'
    print(type)
    p[0] = p[3]


def p_keyboardList(p): #IDs and other types excluded
    '''keyboardList :
    | Q
    | W
    | E
    | R
    | T
    | Y
    | U
    | I
    | O
    | P
    | A
    | S
    | D
    | F
    | G
    | H
    | J
    | K
    | L
    | Z
    | X
    | C
    | V
    | B
    | N
    | M
    | BACKQUOTE
    | TAB
    | CAPSLOCK
    | LSHIFT
    | LCTRL
    | LALT
    | SPACEBAR
    | RALT
    | RCTRL
    | COMMA
    | SLASH
    | RSHIFT
    | PERIOD
    | SEMICOLON
    | QUOTE
    | ENTER
    | RBRACKET
    | LBRACKET
    | BACKSLASH
    | DASH
    | EQUAL
    | BACKSPACE
    | LEFT
    | UP
    | DOWN
    | RIGHT
    '''

    parser = yacc.yacc()


    #From sample calculator parser, this is what allows inputs to be added and used when running:
    # while True:
    #     try:
    #         s = input('calc > ')
    #     except EOFError:
    #         break
    #     if not s: continue
    #     result = parser.parse(s)
    #     print(result)