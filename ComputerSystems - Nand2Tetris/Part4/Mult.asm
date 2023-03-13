// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.
// To multiply using addition, add recursively using a loop
// Put your code here.

@R2
M=0 //initial product is 0

@i
M=0 //loop count is initially 0

//create a loop that will value in R0, R1 times
(LOOP)
//Keep track of loop number
@i
D=M
//Check if loop number and R1 are equal, if yes - exit loop!
@R1
D=D-M
@END
D;JGE

@R0
D=M
//Store the sum in R2
@R2
M=D+M

//increment loop count
@i
M=M+1

//always loop back
@LOOP
0;JMP

(END)
//Termination loop
@END
0;JMP