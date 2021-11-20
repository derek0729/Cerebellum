import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

# reminder to try error detection
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

def p_Scripts(p):  #Scripttypes, Sample and charactercontroller scripts in the works
    '''SAMPLE
    | RIGIDBODY2D'''

def p_SpeedFunc(p): #Defined what speed is
    'SpeedFunc : SPEED EQUALS FLOAT'
    print(type)
    p[0] = p[3]

def p_GravityFunc(p): #Defined what gravity is
    'GravityFunc : GRAVITY EQUALS FLOAT'
    print(type)
    p[0] = p[3]

def p_DirectionFunc(p): #Directionals needed
    '''DirectionFunc : NONE
    | MoveX
    | MoveY'''
    p[0] = p[1]


def p_MovementFunc(p):
    'Movement : ID EQUALS DirectionFunc ID EQUALS DirectionFunc'
    # ^         ^     ^       ^         ^     ^       ^
    #p[0]      p[1]  p[2]    p[3]      p[4]  p[5]    p[6]

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