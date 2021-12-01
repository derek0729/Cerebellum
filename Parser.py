import ply.yacc as yacc
import Lexer
import ScriptAssembler as assemble
tokens = Lexer.tokens
index = []

def p_setScript(p):
    '''script : Regular
                | TopDown
                | Flight'''

def p_Regular_script(p):
    'Regular : REGULAR Speedfunc Movement'
    p[0] = (p[1], p[2], p[3])
    x =p[3]
    assemble.scriptSelect('REGULAR')
    assemble.TwoDMove_start(p[2])
    assemble.TwoDMove_body(x[0], x[1])
    #gen.p_jump_func()
    #gen.p_jump_with_groundcheck_func()
    assemble.p_jump_func_classic()
    assemble.TwoDMove_end()
    assemble.p_jumpMethod()
    assemble.p_groundcheckMethod()
    assemble.p_OnCollisionEnter2D()
    assemble.p_OnCollionExit2D()
    # gen.TwoDMove_end()

    assemble.TwoDMove_end()
    #gen.assplosion()
    # gen.end_simple() enable this for X thing
   

def p_TopDown_script2(p):
    'TopDown : TOPDOWN Speedfunc Movement'
    p[0] = (p[1], p[2], p[3] )
    x = p[3]
    assemble.scriptSelect('TOPDOWN')
    assemble.TwoDMove_start(p[2])
    assemble.TopDownMove_body(x[0], x[1])
    assemble.p_jump_func()
    # gen.p_jump_with_groundcheck_func(p[2])
    assemble.TwoDMove_end()
    assemble.p_groundcheckMethod()
    assemble.p_jumpMethod()
    assemble.TwoDMove_end()
    #gen.assplosion()
    # gen.end_simple() enable this for X thing



def p_Flight_script(p):
    'Flight : FLIGHT Speedfunc Movement'
    p[0] = (p[1], p[2], p[3] )
    x = p[3]
    assemble.scriptSelect('FLIGHT')
    assemble.TwoDMove_start(p[2])
    assemble.TwoDMove_body(x[0], x[1])
    assemble.p_jump_func()
    assemble.TwoDMove_end()
    assemble.p_jumpMethod()
    assemble.p_groundcheckMethod()
    assemble.TwoDMove_end()


def p_speedfunc(p):
    'Speedfunc : Speed EQUALS Float'
    print(type)
    p[0] = (p[3])

def p_movement_rule(p):
    #First move is in x, followed by y , endind with z
    'Movement : ID EQUALS Direction ID EQUALS Direction'
    if p[3] == p[6]:
        print("Directions must not be repeated")
        p_error(p)

    p[0] = p[3], p[6]

def p_Direction(p):
    '''Direction : Horizontal
    | Vertical
    | NONE'''
    p[0] = p[1]

def p_KeyCode(p):
    '''KeyCode : 
          | A
          | B
          | C
          | D
          | E
          | F
          | G
          | H
          | I
          | J
          | K
          | L
          | M
          | N
          | O
          | P
          | Q
          | R
          | S
          | T
          | U
          | V
          | W
          | X
          | Y
          | Z
          | Backspace
          | Tab
          | SysReq
          | Break
          | CapsLock
          | ScrollLock
          | RightShift
          | LeftShift
          | RightControl
          | LeftControl
          | RightAlt
          | LeftAlt
          | RightCommand
          | RightApple
          | LeftCommand
          | LeftWindows
          | RightWindows
          | AltGr
          | Help
          | Print
          | Clear
          | Return
          | Pause
          | Escape
          | Space
          | Exclaim
          | DoubleQuote
          | Hash
          | Dollar
		  | Ampersand
		  | Quote
		  | LeftParen
		  | RightParen
		  | Asterisk
		  | Plus
		  | Comma
		  | Minus
		  | Period
		  | Slash
		  | Colon
		  | Semicolon
		  | Less
		  | Equals
		  | Greater
		  | Question
		  | At
		  | LeftBracket
		  | Backslash
		  | RightBracket
		  | Caret
		  | Underscore
		  | BackQuote
		  
'''
    p[0] = p[1]
    index.append(p[1])
    if check_repeated_keys(index) == True :
        p_error(p)

def p_error(p):
    print("Syntax error in input")
    exit()

def check_repeated_keys(index):
    seen = set()
    for x in index:
        if x in seen:
            print( "Key_"+ x +" Is already being used ")
            return True
        seen.add(x)
    return False

def translate(s):
    try:
        Cerebellum = open(s, 'r')
    except IOError:
        print("Error opening File")
        exit()
    fileScript = Cerebellum.read()
    parser = yacc.yacc()
    output = parser.parse(fileScript)
    assemble.upload()

