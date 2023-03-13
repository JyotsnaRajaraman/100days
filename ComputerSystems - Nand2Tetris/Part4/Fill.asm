// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//CHANGE REQUIRED: Incrementally fill when key is pressed
//when no key is pressed, slowly make screen white again
// Put your code here.

//Variables to remember: 
//SCREEN = screen beginning
//KBD = screen end +1 (or keyboard)

//rough algorithm:
//ptr for where in the screen I am, initialize to SCREEN
//Start an infinite loop
//flag = whether keyboard pressed?
//if flag= yes: 
    //check if ptr <KBD-1
    //if yes: fill ptr with black and then go black
//if flag = no: set ptr to white and then go back
    //check if ptr > SCREEN
    //if yes: fill ptr with white and then go back


//Pointer
@SCREEN
D=A
@ptr
M=D
(LOOP)
    //check if key is pressed
    @KBD
    D=M
    @REDUCE
    D;JEQ // no key, go to REDUCE
    @FILL
    0;JEQ // key, go to FILL

(REDUCE)
    @ptr
    D=M
    @SCREEN
    D=A-D //check if ptr is at screen beginning, if so loop
    @LOOP
    D;JGT
    D=0
    //color pointer white
    @ptr
    A=M
    M=D
    //move pointer back
    @ptr
    M=M-1

    @LOOP
    0;JMP

(FILL)
    @ptr
    D=M
    @KBD
    D=A-D
    //check if ptr is at screen end, if so loop
    @LOOP
    D;JEQ
    D=-1
    //color pointer black
    @ptr
    A=M
    M=D
    //move pointer forward
    @ptr
    M=M+1

    //infinitely loop
    @LOOP
    0;JMP
