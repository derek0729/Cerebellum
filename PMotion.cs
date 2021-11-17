using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PMotion  : MonoBehaviour //our frame work, sin esto no inicializa. This is for the player motion and movements
{
    private float quickness = 1.0f; //movement speed and quickn
    private float bounce = 1f; //jump variable 
    private float gravity = 0.1f; //character's gravity

    float currentX; //variable that returns the value of the current x axis
    float currentY; //variable that returns the value of the  current y axis

    private CharacterController charControl; //creating the character controller 

    private Vector2 charMovement = Vector2.zero; //initializing 2d Vector to 0


    // initialization
    void Start()
    {
        charControl = GetComponent<CharacterController>(); //returning the compo

        if (charControl == null) //no controller was found 
        {
            Debug.LogError("character controller could not be found.");
        }
    }

    
    void FixedUpdate() //get update on the player movement, position etc. in increments of 0.02 game-time seconds. 
    {
        currentX = Input.GetAxis("Horizontal"); //get players x axis
        currentY = Input.GetAxis("Vertical");   //get players y axis 

        charMovement = new Vector2(currentX, currentY); //once i check (x,y) position then update position

        charMovement = transform.TransformDirection(charMovement); //transforming direction from local space to world space. *****could possibly replace this with a transfrom.forward

        charMovement *= quickness;

        if (Input.GetKey(KeyCode.Space) && charControl.isGrounded) //checks if the user pressed any key and if the Character Crontoller was touching the ground during last move
        {
            charMovement.y = bounce; //jump
        }

        if (Input.GetKey(KeyCode.LeftShift))
        {
            charMovement *= 3f;
        }

        charMovement.y -= gravity; //fall back down when jumping, which is why we are subtracting.
        charControl.Move(charMovement); //move
    }
}
