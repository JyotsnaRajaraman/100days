# command lookup tables for various operation types

operations = {
    "add": "//add operation\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n",
    "sub": "//sub operation\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n",
    "and": "//and operation\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n",
    "or": "//or operation\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n",
    "neg": "//neg operation\n@SP\nA=M-1\nM=-M\n",
    "not": "//not operation\n@SP\nA=M-1\nM=!M\n",
    "gt": "//gt operation\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@CONTindex\nD;JGT\n@SP\nA=M-1\nM=0\n(CONTindex)\n",
    "lt": "//less than operation\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@CONTindex\nD;JLT\n@SP\nA=M-1\nM=0\n(CONTindex)\n",
    "eq": "//eq operation\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@CONTindex\nD;JEQ\n@SP\nA=M-1\nM=0\n(CONTindex)\n"
}

pushcommands = {
    "constant": "//push constant\nD=A\n@SP\nAM=M+1\nA=A-1\nM=D\n",
    "local": "//push local\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n",
    "argument": "//push arg\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n",
    "this": "//push this\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n",
    "that": "//push that\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n"
}

popcommands = {
    "local": "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
    "argument": "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
    "this": "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
    "that": "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
    "temp": "@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
}

programflow = {
    "label": "()",
    "goto": "\n0;JMP\n",
    "ifgoto": "@SP\nAM=M-1\nD=M\n"
}
functioncall = {
    "functioncall1": "\nD=A\n@SP\nAM=M+1\nA=A-1\nM=D\n@LCL\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@ARG\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@THIS\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n@THAT\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D",
    "functioncall2": "\n@SP\nD=M-D\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n"
}

functionreturn = {
    "functionreturn": "//functionreturn\n@LCL\nD=M\n@FRAME\nM=D\n@FRAME\nD=M\n@5\nD=D-A\nA=D\nD=M\n@RET\nM=D\n@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@FRAME\nAM=M-1\nD=M\n@THAT\nM=D\n@FRAME\nAM=M-1\nD=M\n@THIS\nM=D\n@FRAME\nAM=M-1\nD=M\n@ARG\nM=D\n@FRAME\nAM=M-1\nD=M\n@LCL\nM=D\n@RET\nA=M\n0;JMP\n"
}

functiondef = {
    "functiondef": "@SP\nAM=M+1\nA=A-1\nM=0\n"
}
