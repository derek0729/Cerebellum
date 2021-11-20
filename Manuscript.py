scripting = ""
def scripts_general(script): #This sets up the prelude to what will be the simplified code generation
    global scripting         #from the parser after the lexical analysis.
    scripting = script       #Variable global scripting acts as an accesible variable for the parser

reference = []
def samplemovement(MoveX):
    piece = "using System.Collections; \n"
    "using System.Collections.Generic; \n"
    "using UnityEngine; \n"
    "\n"
    "public class SampleMovement : MonoBehavior \n"
    "{ \n"
    "public Rigidbody2D rigidb; \n"
    "private float MoveX; \n"
    "void Start() \n"
    "{ \n"
    "rigidb = GetComponent<Rigidbody2D>(); \n"
    "} \n"
    "\n"
    "// Update is called once per frame \n"
    "void FixedUpdate() \n"
    "{ \n"
    "{ \n"
    "MoveX = Input.GetAxisRaw(\"Horizontal\"); \n"
    "rigidb.AddForce(new Vector2(" + MoveX + " * 20, 0)); \n"
    if piece != reference:
        reference.append()