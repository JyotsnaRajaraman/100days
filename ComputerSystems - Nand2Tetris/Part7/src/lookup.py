# command lookup tables
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
