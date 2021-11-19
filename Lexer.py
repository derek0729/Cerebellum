import ply.lex as lex

# Use the ply documentation for reference: https://ply.readthedocs.io/en/latest/ply.html#introduction

# Always declare tokens here in Tokens_list
# List of Keys and other inputs (Update as needed):
tokens = (
    #Scripts
    'SAMPLE', 'RIGIDMOTION',

    #IDs and other types
    'ID', 'FLOAT', 'EQUALS', 'SPEED', 'GRAVITY',

    #Keyboard Letters
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M',

    #Keyboard SpecialKeys
    'BACKQUOTE', 'TAB', 'CAPSLOCK', 'LSHIFT', 'LCTRL', 'LALT', 'SPACEBAR',
    'RALT', 'RCTRL', 'COMMA', 'SLASH', 'RSHIFT', 'PERIOD', 'SEMICOLON', 'QUOTE', 'ENTER',
    'RBRACKET', 'LBRACKET', 'BACKSLASH', 'DASH', 'EQUAL', 'BACKSPACE',
    'LEFT', 'UP', 'DOWN', 'RIGHT',

    #Unity API (Subject to change and experimentation)
    'RIGIDBODY', 'RIGIDBODY2D', 'SLIDERJOINT2D', 'CHARACTERCONTROLLER',

    #Directionals
    'NONE', 'HORIZONTAL', 'VERTICAL'

)  # End of tokens


# def funtion values for tokens as per ply documentation, use format accordingly for future reference

#Scripts
def t_SAMPLE(t):
    r'SAMPLE'
    t.value = 'SAMPLE'

def t_RIGIDMOTION(t):
    r'RIGIDMOTION'
    t.value = 'RIGIDMOTION'


#IDs from Unity
def t_SPEED(t):
    r'SPEED'
    t.type = 'SPEED'

def t_GRAVITY(t):
    r'GRAVITY'
    t.type = 'GRAVITY'

# Keyboard Letters
def t_Q(t):
    r'Letter_Q'
    t.value = 'Q'
    return t


def t_W(t):
    r'Letter_W'
    t.value = 'W'
    return t


def t_E(t):
    r'Letter_E'
    t.value = 'E'
    return t


def t_R(t):
    r'Letter_R'
    t.value = 'R'
    return t


def t_T(t):
    r'Letter_T'
    t.value = 'E'
    return t


def t_Y(t):
    r'Letter_Y'
    t.value = 'Y'
    return t


def t_U(t):
    r'Letter_U'
    t.value = 'U'
    return t


def t_I(t):
    r'Letter_I'
    t.value = 'I'
    return t


def t_O(t):
    r'Letter_O'
    t.value = 'O'
    return t


def t_P(t):
    r'Letter_P'
    t.value = 'P'
    return t


def t_A(t):
    r'Letter_A'
    t.value = 'A'
    return t


def t_S(t):
    r'Letter_S'
    t.value = 'S'
    return t


def t_D(t):
    r'Letter_D'
    t.value = 'D'
    return t


def t_F(t):
    r'Letter_F'
    t.value = 'F'
    return t


def t_G(t):
    r'Letter_G'
    t.value = 'G'
    return t


def t_H(t):
    r'Letter_H'
    t.value = 'H'
    return t


def t_J(t):
    r'Letter_J'
    t.value = 'J'
    return t


def t_K(t):
    r'Letter_K'
    t.value = 'K'
    return t


def t_L(t):
    r'Letter_L'
    t.value = 'L'
    return t


def t_Z(t):
    r'Letter_Z'
    t.value = 'Z'
    return t


def t_X(t):
    r'Letter_X'
    t.value = 'X'
    return t


def t_C(t):
    r'Letter_C'
    t.value = 'C'
    return t


def t_V(t):
    r'Letter_V'
    t.value = 'V'
    return t


def t_B(t):
    r'Letter_B'
    t.value = 'B'
    return t


def t_N(t):
    r'Letter_N'
    t.value = 'N'
    return t


def t_M(t):
    r'Letter_M'
    t.value = 'M'
    return t


# IDs and other types

reserved = {  # reserved words for conflict prevension
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE'
}


def t_ID(t):  # This should check for reserved words
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # This should match any letter or digit
    t.type = reserved.get(t.value, 'ID')
    return t


t_FLOAT = r'[0-9]+[.][0-9]+' #Should allow more than one combination of digits, followed by another combination

t_EQUALS = r'\='

t_ignore = ' \t'


# Keyboard SpecialCharacters

def t_BACKQUOTE(t):
    r'KChar_BACKQUOTE'
    t.value = 'BACKQUOTE'
    return t


def t_TAB(t):
    r'KChar_TAB'
    t.value = 'TAB'
    return t


def t_CAPSLOCK(t):
    r'KChar_CAPSLOCK'
    t.value = 'CAPSLOCK'
    return t


def t_LSHIft(t):
    r'KChar_LSHIFT'
    t.value = 'LSHIFT'
    return t


def t_LCTRL(t):
    r'KChar_LCTRL'
    t.value = 'LCTRL'
    return t


def t_LALT(t):
    r'KChar_LALT'
    t.value = 'LALT'
    return t


def t_SPACEBAR(t):
    r'KChar_SPACEBAR'
    t.value = 'SPACEBAR'
    return t


def t_RALT(t):
    r'KChar_RALT'
    t.value = 'RALT'
    return t


def t_RCTRL(t):
    r'KChar_RCTRL'
    t.value = 'RCTRL'
    return t


def t_COMMA(t):
    r'KChar_COMMA'
    t.value = 'COMMA'
    return t


def t_SLASH(t):
    r'KChar_SLASH'
    t.value = 'SLASH'
    return t


def t_RSHIFT(t):
    r'KChar_RSHIFT'
    t.value = 'RSHIFT'
    return t


def t_PERIOD(t):
    r'KChar_PERIOD'
    t.value = 'PERIOD'
    return t


def t_SEMICOLON(t):
    r'KChar_SEMICOLON'
    t.value = 'SEMICOLON'
    return t


def t_QUOTE(t):
    r'KChar_QUOTE'
    t.value = 'QUOTE'
    return t


def t_ENTER(t):
    r'KChar_ENTER'
    t.value = 'ENTER'
    return t


def t_RBRACKET(t):
    r'KChar_RBRACKET'
    t.value = 'RBRACKET'
    return t


def t_LBRACKET(t):
    r'KChar_LBRACKET'
    t.value = 'LBRACKET'
    return t


def t_BACKSLASH(t):
    r'KChar_BACKSLASH'
    t.value = 'BACKSLASH'
    return t


def t_DASH(t):
    r'KChar_DASH'
    t.value = 'DASH'
    return t


def t_EQUAL(t):
    r'KChar_EQUAL'
    t.value = 'EQUAL'
    return t


def t_BACKSPACE(t):
    r'KChar_BACKSPACE'
    t.value = 'BACKSPACE'
    return t


# Keyboard Directionals

def t_HORIZONTAL(t):
    r'Directional_LEFT'
    t.value = 'LEFT'
    return t


def t_VERTICAL(t):
    r'Directional_UP'
    t.value = 'UP'
    return t

def t_NONE(t):
    r'Directional_NONE'
    t.value = 'NONE'
    return t

def t_RIGIDBODY(t):
    r'RIGIDBODY'
    t.value = 'RIGIDBODY'
    return t

def t_RIGIDBODY2D(t):
    r'RIGIDBODY2D'
    t.value = 'RIGIDBODY2D'
    return t

def t_SLIDERJOINT2D(t):
    r'SLIDERJOINT2D'
    t.value = 'SLIDERJOINT2D'
    return t

def t_CHARACTERCONTROLLER(t):
    r'CHARACTERCONTROLLER'
    t.value = 'CHARACTERCONTROLLER'
    return t


# Error handling from documentation:
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex() #Builds the lexer