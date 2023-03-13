from lookup import operations, pushcommands, popcommands, functioncall, functiondef, functionreturn, programflow

# to translate operations
# this includes add,sub,and,or,gt,lt,eq,not,neg


def translateops(line):
    return operations.get(line)

# to translate push commands
# for constant,local, this, that, argument, temp, pointer, static


def translatepush(line, nameoffile):
    pushtype = line.split(" ")[0]
    number = line.split(" ")[1]

    if pushtype == "constant":
        return "@" + number + "\n" + pushcommands.get(pushtype)
    elif pushtype == "local":
        return "@LCL\nD=M\n@" + number + "\n" + pushcommands.get(pushtype)
    elif pushtype == "argument":
        return "@ARG\nD=M\n@" + number + "\n" + pushcommands.get(pushtype)
    elif pushtype == "this":
        return "@THIS\nD=M\n@" + number + "\n" + pushcommands.get(pushtype)
    elif pushtype == "that":
        return "@THAT\nD=M\n@" + number + "\n" + pushcommands.get(pushtype)
    elif pushtype == "temp":
        number = str(int(number)+5)
        return "//push temp\n@"+number+"\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n"
    elif pushtype == "static":
        return "//push static\n@"+nameoffile + "." + number+"\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n"
    elif pushtype == "pointer":
        if number == "0":
            return "//push pointer0\n@THIS\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n"
        else:
            return "//push pointer1\n@THAT\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n"

# to translate pop commands
# for constant,local, this, that, argument, temp, pointer, static


def translatepop(line, nameoffile):
    poptype = line.split(" ")[0]
    number = line.split(" ")[1]
    if poptype == "local":
        return "//pop local\n@LCL\nD=M\n@" + number + "\n" + popcommands.get(poptype)
    elif poptype == "argument":
        return "//pop arg\n@ARG\nD=M\n@" + number + "\n" + popcommands.get(poptype)
    elif poptype == "this":
        return "//pop this\n@THIS\nD=M\n@" + number + "\n" + popcommands.get(poptype)
    elif poptype == "that":
        return "//pop that\n@THAT\nD=M\n@" + number + "\n" + popcommands.get(poptype)
    elif poptype == "temp":
        number = str(int(number)+5)
        return "//pop temp\n@" + number + "\nD=A\n" + popcommands.get(poptype)
    elif poptype == "static":
        return "//pop static\n@SP\nAM=M-1\nD=M\n@"+nameoffile + "." + number+"\nM=D\n"
    elif poptype == "pointer":
        if number == "0":
            return "//pop pointer0\n@SP\nAM=M-1\nD=M\n@THIS\nM=D\n"
        else:
            return "//pop pointer1\n@SP\nAM=M-1\nD=M\n@THAT\nM=D\n"

#to translate function definition

def translatefuncdef(line):
    func = line.split(" ")[0]
    number = int(line.split(" ")[1])
    return "//functiondef\n(" + func + ")\n" + number * functiondef.get("functiondef")

#to translate return
def translatefuncreturn():
    return functionreturn.get("functionreturn")

#to translate function call

def translatefunctioncall(line, labelcount):
    number = 0
    #arg number may not be specified, like in call Sys.init
    if len(line.split(" ")) == 1:
        func = line.split(" ")[0]
    else:
        func = line.split(" ")[0]
        number = int(line.split(" ")[1])
    num = str(number + 5)
    label = "(" + func + "$" + str(labelcount) + ")"
    translatedline = "@" + label[1:-1] + functioncall.get("functioncall1") + "\n@" + num + "\nD=A" + functioncall.get("functioncall2") + \
        "@" + func + "\n0;JMP\n" + label + "\n"
    return translatedline


# translate code

def translate(lines, nameoffile=""):
    outputlines = []
    # to ensure that labels aren't repeated
    labelcounter = 0
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        op = line.split(" ")[0]
        # check if it is a operation
        if op in ['add', 'sub', 'and', 'or', 'gt', 'lt', 'eq', 'not', 'neg']:
            translatedline = translateops(op)
            # if it is in a compare, then it needs a label
            if op in ['gt', 'lt', 'eq']:
                translatedline = translatedline.replace(
                    'index', str(labelcounter))
                labelcounter += 1
            outputlines.append(translatedline)
        # check whether push
        elif op == "push":
            outputlines.append(translatepush(line[5:], nameoffile))
        # check whether pop
        elif op == "pop":
            outputlines.append(translatepop(line[4:], nameoffile))
        elif op == "label":
            outputlines.append("("+nameoffile+"$"+line[6:]+")\n")
        elif op == "goto":
            outputlines.append("@"+nameoffile+"$" +
                               line[5:]+programflow.get("goto"))
        elif op == "if-goto":
            outputlines.append(programflow.get(
                "ifgoto")+"@"+nameoffile+"$"+line[8:]+"\nD;JNE\n")
        elif op == "function":
            outputlines.append(translatefuncdef(line[9:]))
        elif op == "return":
            outputlines.append(translatefuncreturn())
        elif op == "call":
            outputlines.append(translatefunctioncall(
                line[5:], labelcounter))
            labelcounter += 1
    return outputlines
