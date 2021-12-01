using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class TwoDMoveManual: MonoBehaviour 
 { 
float movespeed = 1.0f;
Rigidbody2D rB; 
float moveX; 
float moveY; 
string Xaxis = "Horizontal"; 
string Yaxis = "NONE"; 
float ground = 1f; 
public bool touchground; 
void Start() 
{ 
rB = gameObject.GetComponent<Rigidbody2D>(); 
} 
void Update() 
{ 
moveX = Input.GetAxisRaw(Xaxis); 
moveY = Input.GetAxisRaw(Yaxis); 
} 
private void FixedUpdate() 
{ 
Vector2 moveVector = new Vector2(moveX, moveY) * movespeed; 
rB.AddForce(moveVector * movespeed, ForceMode2D.Impulse); 
if (Input.GetKey(KeyCode.Space) && groundcheck()) { 
jump(); 
} 
} 
void jump() { 
rB.AddForce(new Vector2(0, 1), ForceMode2D.Impulse); 
} 
bool groundcheck() { 
return Physics2D.Raycast(transform.position, Vector2.down, ground); 
} 
} 
