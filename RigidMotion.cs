
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class RigidMotion : MonoBehaviour
{
    float quickness = 8.0f;

    string Xaxis = "Horizontal"; //created this this for the 'GetAxis(string axisName) method
    string Yaxis = "Vertical"; //axisName, in this case 'Y axis'

    Rigidbody2D rigidBod; //creating a 2D rigid body, to apply 

    float shiftX;//move x and y
    float shiftY;

    float groundGap = 1f; //distance to ground
    void Start()
    {
        rigidBod = this.GetComponent<Rigidbody2D>(); //Returning the character compoment
        if (rigidBod == null)
        {
            Debug.LogError("The Rigid body was not found."); //no RigidBody was found 
        }
    }
    void Update()//here we are getting a refresh of the players (game object) position 
    {
        shiftX = Input.GetAxis(Xaxis); //update me (refresh) on x axis position. Returns the value of the virtual axis identified by axisName. 
        shiftY = Input.GetAxis(Yaxis); //update me (refresh) on Y axis position 
    }
    void FixedUpdate()  //calculates and applies game physics to our game object in increments of 0.02 game-time seconds.
    {
        Vector2 vectorMove = new Vector2(0.0f, 1.0f) * quickness;

        rigidBod.AddForce(vectorMove, (ForceMode2D)ForceMode.Acceleration); //adding physics provided by rigidBody

        if (Input.GetKey(KeyCode.Space) && isGrounded()) //checks if the user pressed any key and if the object was touching the ground during last move
        {
            jump();
        }
        if (Input.GetKey(KeyCode.LeftShift))
        {
            dash(vectorMove);
        }
        if (Input.GetKey(KeyCode.X))
        {
            jump();
        }

    }
    bool isGrounded()
    {
        return Physics.Raycast(transform.position, Vector2.down, groundGap); //Casts a ray against all colliders in the Scene, reporting the distance between the current object and the reported Collider (what was hit)

    }

    void jump()
    {
        rigidBod.AddForce(new Vector2(0, 0), (ForceMode2D)ForceMode.Impulse);
    }
    void dash(Vector2 vectorMove)
    {
       rigidBod.AddForce(vectorMove * 3f, (ForceMode2D)ForceMode.Force); //we are creating a vector similar to the one created at the beginning of FixedUpdate() with a higher float multiplied and force added
    }
} 

   