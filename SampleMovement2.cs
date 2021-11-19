using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SampleMovement2 : MonoBehaviour
{
    public Rigidbody2D rigidb;
    private float MoveX;
    void Start()
    {
        rigidb = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
    {
        MoveX = Input.GetAxisRaw("Horizontal");
        rigidb.AddForce(new Vector2(MoveX * 20, 0)); 
    }
}