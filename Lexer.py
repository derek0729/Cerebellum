
import ply.lex as lex

tokens = (

#Scripts
	'REGULAR', 'TOPDOWN', 'FLIGHT',
#Identifiers and others
	'ID', 'Float', 'EQUALS', 'Speed',
#Dirrectionals
	'Horizontal', 'Vertical', 'NONE',
#Keyboard and Unity recognized keys
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M',
	'Backspace','Tab', 'SysReq','Break', 'CapsLock', 'ScrollLock', 'RightShift', 'LeftShift',
    'RightControl', 'LeftControl', 'RightAlt', 'LeftAlt', 'RightCommand', 'RightApple', 'LeftCommand', 'LeftWindows',
    'RightWindows', 'AltGr', 'Help','Print', 'Clear', 'Return', 'Pause', 'Escape',
    'Space', 'Exclaim','DoubleQuote','Hash', 'Dollar', 'Ampersand', 'Quote', 'LeftParen',
    'RightParen', 'Asterisk', 'Plus', 'Comma', 'Minus', 'Period', 'Slash', 'Colon', 'Semicolon',
    'Less', 'Equals', 'Greater', 'Question', 'At', 'LeftBracket', 'Backslash', 'RightBracket', 'Caret', 'Underscore','BackQuote',
)

#Scripts
def t_REGULAR(t):
    r'REGULAR'
    t.value = 'REGULAR'
    return t

def t_TOPDOWN(t):
    r'TOPDOWN'
    t.value = 'TOPDOWN'
    return t

def t_FLIGHT(t):
    r'FLIGHT'
    t.value = 'FLIGHT'
    return t

#Directionals
def t_Horizontal(t):
    r'Horizontal'
    t.select = 'Horizontal'
    return t

def t_Speed(t):
    r'Speed'
    t.select = 'Speed'
    return t

def t_Vertical(t):
    r' Vertical '
    t.value = 'Vertical'
    return t
	
def t_NONE(t):
    r'NONE'
    t.value = 'NONE'
    return t

#Keyboard
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
    t.value = 'T'
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

#Unity friendly keys
def t_Backspace(t):
    r'Key_Backspace'
    t.value = 'Backspace'
    return t

def t_Tab(t):
    r'Key_Tab'
    t.value = 'Tab'
    return t

def t_SysReq(t):
    r'Key_SysReq'
    t.value = 'SysReq'
    return t

def t_Break(t):
    r'Key_Break'
    t.value = 'Break'
    return t

def t_CapsLock(t):
    r'Key_CapsLock'
    t.value = 'CapsLock'
    return t

def t_ScrollLock(t):
    r'Key_ScrollLock'
    t.value = 'ScrollLock'
    return t

def t_RightShift(t):
    r'Key_RightShift'
    t.value = 'RightShift'
    return t

def t_LeftShift(t):
    r'Key_LeftShift'
    t.value = 'LeftShift'
    return t

def t_RightControl(t):
    r'Key_RightControl'
    t.value = 'RightControl'
    return t

def t_RightAlt(t):
    r'Key_RightAlt'
    t.value = 'RightAlt'
    return t

def t_LeftAlt(t):
    r'Key_LeftAlt'
    t.value = 'LeftAlt'
    return t

def t_RightCommand(t):
    r'Key_RightCommand'
    t.value = 'RightCommand'
    return t

def t_RightApple(t):
    r'Key_RightApple'
    t.value = 'RightApple'
    return t

def t_LeftCommand(t):
    r'Key_LeftCommand'
    t.value = 'LeftCommand'
    return t

def t_LeftWindows(t):
    r'Key_LeftWindows'
    t.value = 'LeftWindows'
    return t

def t_RightWindows(t):
    r'Key_RightWindows'
    t.value = 'RightWindows'
    return t

def t_AltGr(t):
    r'Key_AltGr'
    t.value = 'AltGr'
    return t

def t_Help(t):
    r'Key_Help'
    t.value = 'Help'
    return t

def t_Print(t):
    r'Key_Print'
    t.value = 'Print'
    return t

def t_Clear(t):
    r'Key_Clear'
    t.value = 'Clear'
    return t

def t_Return(t):
    r'Key_Return'
    t.value = 'Return'
    return t

def t_Pause(t):
    r'Key_Pause'
    t.value = 'Pause'
    return t

def t_Escape(t):
    r'Key_Escape'
    t.value = 'Escape'
    return t

def t_Space(t):
    r'Key_Space'
    t.value = 'Space'
    return t

def t_Exclaim(t):
    r'Key_Exclaim'
    t.value = 'Exclaim'
    return t

def t_DoubleQuote(t):
    r'Key_DoubleQuote'
    t.value = 'DoubleQuote'
    return t

def t_Hash(t):
    r'Key_Hash'
    t.value = 'Hash'
    return t

def t_Dollar(t):
    r'Key_Dollar'
    t.value = 'Dollar'
    return t

def t_Ampersand(t):
    r'Key_Ampersand'
    t.value = 'Ampersand'
    return t

def t_Quote(t):
    r'Key_Quote'
    t.value = 'Quote'
    return t

def t_LeftParen(t):
    r'Key_LeftParen'
    t.value = 'LeftParen'
    return t

def t_RightParen(t):
    r'Key_RightParen'
    t.value = 'RightParen'
    return t

def t_Asterisk(t):
    r'Key_Asterisk'
    t.value = 'Asterisk'
    return t

def t_Plus(t):
    r'Key_Plus'
    t.value = 'Plus'
    return t

def t_Comma(t):
    r'Key_Comma'
    t.value = 'Comma'
    return t

def t_Minus(t):
    r'Key_Minus'
    t.value = 'Minus'
    return t

def t_Period(t):
    r'Key_Period'
    t.value = 'Period'
    return t

def t_Slash(t):
    r'Key_Slash'
    t.value = 'Slash'
    return t

def t_Colon(t):
    r'Key_Colon'
    t.value = 'Colon'
    return t

def t_Semicolon(t):
    r'Key_Semicolon'
    t.value = 'Semicolon'
    return t

def t_Less(t):
    r'Key_Less'
    t.value = 'Less'
    return t

def t_Equals(t):
    r'Key_Equals'
    t.value = 'Equals'
    return t

def t_Greater(t):
    r'Key_Greater'
    t.value = 'Greater'
    return t

def t_Question(t):
    r'Key_Question'
    t.value = 'Question'
    return t

def t_At(t):
    r'Key_At'
    t.value = 'At'
    return t

def t_LeftBracket(t):
    r'Key_LeftBracket'
    t.value = 'LeftBracket'
    return t

def t_Backslash(t):
    r'Key_Backslash'
    t.value = 'Backslash'
    return t

def t_RightBracket(t):
    r'Key_RightBracket'
    t.value = 'RightBracket'
    return t

def t_Caret(t):
    r'Key_Caret'
    t.value = 'Caret'
    return t

def t_Underscore(t):
    r'Key_Underscore'
    t.value = 'Underscore'
    return t

def t_BackQuote(t):
    r'Key_BackQuote'
    t.value = 'BackQuote'
    return t

t_Float = r'[[0-9]+[.][0-9]+'
t_EQUALS = r'\='
t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.select = 'ID'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

#initializes lexer
lexer = lex.lex()

try:
   CerebellumLauncher = open("Launch.txt", 'r')
except IOError:
   print("Error opening file")
   exit()

fileText = CerebellumLauncher.read()
lexer.input(fileText)

# Tokenize

while True:
  tok = lexer.token()
  if not tok:
     break      # No more input
  print(tok)
