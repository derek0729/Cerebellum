import ply.yacc as yacc
import Lexer
from Lexer import tokens


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