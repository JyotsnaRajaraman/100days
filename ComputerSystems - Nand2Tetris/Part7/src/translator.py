from lookup import operations, pushcommands, popcommands

# to translate operations
# this includes add,sub,and,or,gt,lt,eq,not,neg


def translateops(line):
    return operations.get(line)

# to translate push commands
# for constant,local, this, that, argument, temp, pointer, static


def translatepush(line, nameoffile):
    for index, char in enumerate(line):
        if char.isdigit():
            pushtype = line[:index]
            number = line[index:]
            break
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
    for index, char in enumerate(line):
        if char.isdigit():
            poptype = line[:index]
            number = line[index:]
            break
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

# translates code


def translate(lines, nameoffile):
    outputlines = []
    # to ensure that labels aren't repeated
    labelcounter = 0
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        # check if it is a operation
        if line in ['add', 'sub', 'and', 'or', 'gt', 'lt', 'eq', 'not', 'neg']:
            translatedline = translateops(line)
            # if it is in a compare, then it needs a label
            if line in ['gt', 'lt', 'eq']:
                translatedline = translatedline.replace(
                    'index', str(labelcounter))
                labelcounter += 1
            outputlines.append(translatedline)
        # check whether push
        elif line[:4] == "push":
            outputlines.append(translatepush(line[4:], nameoffile))
        # check whether pop
        elif line[:3] == "pop":
            outputlines.append(translatepop(line[3:], nameoffile))
    return outputlines
