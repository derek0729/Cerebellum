code = []

select = ""

def scriptSelect(sct):
    global select
    select = sct
    print(select)


def TwoDMove_start(speed):
    block = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "public class TwoDMoveManual: MonoBehaviour \n { \n" \
            "float movespeed = " + speed + "f;\n"
    if code != block:
        code.append(block)

def TwoDMove_body(x, y):
   block = "Rigidbody2D rB; \n"\
           "float moveX; \n"\
           "float moveY; \n"\
           "string Xaxis = \"" + x + "\"; \n"\
            "string Yaxis = \"" + y + "\"; \n"\
            "float ground = 1f; \n"\
            "public bool touchground; \n"\
            "void Start() \n"\
            "{ \n"\
            "rB = gameObject.GetComponent<Rigidbody2D>(); \n"\
            "} \n" \
            "void Update() \n"\
            "{ \n"\
            "moveX = Input.GetAxisRaw(Xaxis); \n"\
            "moveY = Input.GetAxisRaw(Yaxis); \n"\
            "} \n"\
            "private void FixedUpdate() \n"\
            "{ \n"\
            "Vector2 moveVector = new Vector2(moveX, moveY) * movespeed; \n"\
            "rB.AddForce(moveVector * movespeed, ForceMode2D.Impulse); \n"
   code.append(block)

def TopDownMove_body(x, y):
   block = "Rigidbody2D rB; \n"\
           "float moveX; \n"\
           "float moveY; \n"\
           "string Xaxis = \"" + x + "\"; \n"\
            "string Yaxis = \"" + y + "\"; \n"\
            "float ground = 1f; \n"\
            "void Start() \n"\
            "{ \n"\
            "rB = gameObject.GetComponent<Rigidbody2D>(); \n"\
            "Physics2D.gravity = Vector2.zero; \n"\
            "} \n" \
            "void Update() \n"\
            "{ \n"\
            "moveX = Input.GetAxisRaw(Xaxis); \n"\
            "moveY = Input.GetAxisRaw(Yaxis); \n"\
            "} \n"\
            "private void FixedUpdate() \n"\
            "{ \n"\
            "Vector2 moveVector = new Vector2(moveX, moveY) * movespeed; \n"\
            "rB.AddForce(moveVector * movespeed, ForceMode2D.Impulse); \n"
   code.append(block)

def p_jump_func():
    block = "if (Input.GetKey(KeyCode.Space) && groundcheck()) { \n"\
    "jump(); \n"\
    "} \n"
    code.append(block)

def p_jump_func_classic():
    block = "if (Input.GetKey(KeyCode.Space) && groundcheck() && touchground) { \n" \
            "jump(); \n" \
            "} \n"
    code.append(block)

def p_jumpMethod():
    block = "void jump() { \n"\
    "rB.AddForce(new Vector2(0, 1), ForceMode2D.Impulse); \n"\
    "} \n"
    code.append(block)

def p_jump_with_groundcheck_func():
    block = "if (Input.GetKey(KeyCode.Space) && groundcheck()) { \n"\
    "jump(); \n"\
    "} \n"

def p_groundcheckMethod():
    block = "bool groundcheck() { \n"\
    "return Physics2D.Raycast(transform.position, Vector2.down, ground); \n"\
    "} \n"
    code.append(block)

def p_OnCollisionEnter2D():
    block = "private void OnCollisionEnter2D(Collision2D collision) { \n"\
    "touchground = true; \n"\
    "} \n"
    code.append(block)

def p_OnCollionExit2D():
    block = "private void OnCollisionExit2D(Collision2D collision) { \n"\
    "touchground = false; \n"\
    "} \n"
    code.append(block)

def TwoDMove_end():
    block = "} \n"
    code.append(block)

def upload():
    final_code = code[0]

    for block in code:
        if final_code != block:
            final_code += block
    if select == 'TOPDOWN':
        file = open("TopDownMovement.cs", 'w')
    elif select == 'FLIGHT':
        file = open("FlightMovement.cs", 'w')
    else:
        file = open("RegularMovement.cs", 'w')
        
    file.write(final_code)
    file.close()
