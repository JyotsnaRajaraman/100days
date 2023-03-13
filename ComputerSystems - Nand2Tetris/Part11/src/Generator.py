# Symbol tables and code generation

global subroutine_symbols
global symbol_table

# when starting, no symbols added in both subroutine and symbol tables
subroutine_symbols = {}

# stores kind, type, field_count details
symbol_table = {}

# initialize count variables
field_count = 0
static_count = 0
subroutine_total = 0
argument_count = 0
varcount = 0
local_count = 0

# symbols for each subroutine


def initialize_subroutine_symbols():
    global local_count
    global subroutine_table
    global argument_count
    global subroutine_total
    subroutine_table = {}
    argument_count = 0
    local_count = 0
    subroutine_total = 0


# lookups for types/kinds/unary/operations
types = ['int', 'char', 'boolean']
operations = {'+': 'add\n', '-': 'sub\n', '&amp;': 'and\n', '|': 'or\n', '&gt;': 'gt\n',
              '&lt;': 'lt\n', '=': 'eq\n', '*': 'call Math.multiply 2\n', '/': 'call Math.divide 2\n'}
unaryoperationserations = {'-', '~'}
unary_code = {'-': 'neg\n', '~': 'not\n'}
keywordConstant = {'true', 'false', 'null', 'this'}
statements = {'letStatement', 'ifStatement',
              'whileStatement', 'doStatement', 'returnStatement'}
op = {'+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '='}

# function to generate code from tokens generated


def Generator(code_syntax):
    global indexOf
    indexOf = 0
    # tokens so far
    token_syntax = []
    # generated code
    compiled_code = []
    for line in code_syntax:
        # split to index into it
        line = line.split()
        if (len(line) > 0):
            token_syntax.append(line)
    # if there are no tokens, nothing to generate
    if (len(token_syntax) > 0):
        return writeClass(token_syntax, compiled_code)


def writeClass(token_syntax, compiled_code):
    global indexOf
    global currentClassName
    indexOf += 2
    # for class name
    currentClassName = token_syntax[indexOf][1]
    indexOf += 2
    # within <classVarDec>
    # add to symbol table
    while (token_syntax[indexOf][0] == '<classVarDec>'):
        writeClassVarDec(token_syntax)
        indexOf += 1
    # within <subroutineDec>
    while (token_syntax[indexOf][0] == '<subroutineDec>'):
        writesubroutineDec(token_syntax, compiled_code)
        indexOf += 1
    indexOf += 1
    return compiled_code


def writeClassVarDec(token_syntax):

    global indexOf
    global symbol_table
    global static_count
    global field_count

    indexOf += 1
    kind = token_syntax[indexOf][1]
    indexOf += 1
    # based on data type (primitive)
    if token_syntax[indexOf][1] in ['int', 'char', 'boolean']:
        type = token_syntax[indexOf][1]
    else:
        type = token_syntax[indexOf][1]
    indexOf += 1
    name = token_syntax[indexOf][1]
    indexOf += 1

    # add to symbol table
    if kind == 'static':
        symbol_table[name] = [kind, type, static_count]
        static_count += 1
    else:
        symbol_table[name] = [kind, type, field_count]
        field_count += 1
    while (token_syntax[indexOf][1] == ','):
        indexOf += 1
        name = token_syntax[indexOf][1]
        indexOf += 1
        # add to symbol table
        if kind == 'static':
            symbol_table[name] = [kind, type, static_count]
            static_count += 1
        else:
            symbol_table[name] = [kind, type, field_count]
            field_count += 1
    indexOf += 1


def writeLet(token_syntax, compiled_code):
    # for let
    global indexOf
    global subroutine_symbols
    # need to skip the </> lines
    indexOf += 2
    variable = token_syntax[indexOf][1]
    indexOf += 1
    # expression
    if token_syntax[indexOf][1] != '[':
        indexOf += 1
        writeExpression(token_syntax, compiled_code)
        indexOf += 1
        # check what type of var and write appropriate code
        if variable in subroutine_symbols:
            compiled_code.append(
                "pop " + subroutine_symbols[variable][0] + " " + str(subroutine_symbols[variable][2]) + "\n")
        elif variable in symbol_table:
            if symbol_table[variable][0] == "field":
                compiled_code.append(
                    "pop this " + str(symbol_table[variable][2]) + "\n")
            else:
                compiled_code.append(
                    "pop " + symbol_table[variable][0] + " " + str(symbol_table[variable][2]) + "\n")
        indexOf += 1
    else:
        indexOf += 1
        writeExpression(token_syntax, compiled_code)
        indexOf += 2
        compiled_code.append("push " + subroutine_symbols[variable][0] + " " + str(
            subroutine_symbols[variable][2]) + "\n" + "add\n")
        indexOf += 1
        writeExpression(token_syntax, compiled_code)
        indexOf += 1
        # wrap up the function
        compiled_code.append(
            "pop temp 0\npop pointer 1\npush temp 0\npop that 0\n")
        indexOf += 1


def writeDo(token_syntax, compiled_code):
    # for do function
    global indexOf
    global subroutine_symbols
    global symbol_table
    indexOf += 2
    id1 = token_syntax[indexOf][1]
    indexOf += 1
    if token_syntax[indexOf][1] == '.':
        indexOf += 1
        id2 = token_syntax[indexOf][1]
        indexOf += 1
        if id1 in subroutine_symbols:
            # find the kind and type to write code
            kind = subroutine_symbols[id1][0]
            type = subroutine_symbols[id1][1]
            ind = str(subroutine_symbols[id1][2])
            if kind == "field":
                kind = "this"
            compiled_code.append("push " + kind + " " + ind + "\n")
        elif id1 in symbol_table:
            kind = symbol_table[id1][0]
            type = symbol_table[id1][1]
            ind = str(symbol_table[id1][2])
            if kind == "field":
                kind = "this"
            compiled_code.append("push " + kind + " " + ind + "\n")
        else:
            type = ""
        indexOf += 1
        nP = writeExpressionList(token_syntax, compiled_code)
        indexOf += 3
        if id1 in symbol_table or id1 in subroutine_symbols:
            compiled_code.append("call " + type + "." + id2 +
                                 " " + str(nP+1) + "\npop temp 0\n")
        else:
            compiled_code.append("call " + id1 + "." + id2 +
                                 " " + str(nP) + "\npop temp 0\n")
    else:
        compiled_code.append("push pointer 0\n")
        indexOf += 1
        nP = writeExpressionList(token_syntax, compiled_code)
        indexOf += 3
        compiled_code.append("call " + currentClassName + "." +
                             id1 + " " + str(nP+1) + "\npop temp 0\n")


def writeReturn(token_syntax, compiled_code):
    # for return
    global indexOf
    indexOf += 2
    if token_syntax[indexOf][0][1:-1] == 'expression':
        writeExpression(token_syntax, compiled_code)
        indexOf += 1
        compiled_code.append("return\n")
    else:
        # return code
        compiled_code.append("push constant 0\nreturn\n")
    indexOf += 1

# for both if and while the general code layout is defined,
# compile expression and go to for ~output


def writeWhile(token_syntax, compiled_code):
    # for while
    global indexOf
    global varcount
    tempcount = varcount
    varcount += 2
    indexOf += 3
    compiled_code.append("label "+currentClassName+"."+str(tempcount)+"\n")
    writeExpression(token_syntax, compiled_code)
    indexOf += 2
    compiled_code.append("not\nif-goto "+currentClassName +
                         "."+str(tempcount+1)+"\n")
    indexOf += 1
    writeStatements(token_syntax, compiled_code)
    indexOf += 2
    compiled_code.append("goto "+currentClassName+"."+str(tempcount) +
                         "\n"+"label "+currentClassName+"."+str(tempcount+1)+"\n")


def writeIf(token_syntax, compiled_code):
    # for if
    global indexOf
    global varcount
    tempcount = varcount
    varcount += 2
    indexOf += 3
    writeExpression(token_syntax, compiled_code)
    indexOf += 3
    compiled_code.append(
        "not\nif-goto "+currentClassName+"."+str(tempcount)+"\n")
    writeStatements(token_syntax, compiled_code)
    indexOf += 2
    compiled_code.append("goto "+currentClassName+"."+str(tempcount+1) +
                         "\n"+"label "+currentClassName+"."+str(tempcount)+"\n")
    if token_syntax[indexOf][0] == '<keyword>' and token_syntax[indexOf][1] == 'else':
        indexOf += 2
        writeStatements(token_syntax, compiled_code)
        indexOf += 2
    compiled_code.append("label "+currentClassName+"."+str(tempcount+1)+"\n")


def writeStatements(token_syntax, compiled_code):
    # write statements within <statements></statements>
    global indexOf
    indexOf += 1
    while (token_syntax[indexOf][0] != "</statements>"):
        statement_type = token_syntax[indexOf][0][1:-1]
        f[statement_type](token_syntax, compiled_code)
        indexOf += 1


def writeVarDec(token_syntax):
    # add symbols
    global indexOf
    global subroutine_symbols
    global local_count
    global subroutine_total
    indexOf += 2
    kind = 'local'
    if token_syntax[indexOf][1] in ['int', 'char', 'boolean']:
        type = token_syntax[indexOf][1]
    else:
        type = token_syntax[indexOf][1]
    indexOf += 1
    name = token_syntax[indexOf][1]
    indexOf += 1
    subroutine_symbols[name] = [kind, type, local_count]
    local_count += 1
    subroutine_total += 1
    while (token_syntax[indexOf][1] == ','):
        indexOf += 1
        name = token_syntax[indexOf][1]
        indexOf += 1
        subroutine_symbols[name] = [kind, type, local_count]
        local_count += 1
        subroutine_total += 1
    indexOf += 1


def writesubroutineDec(token_syntax, compiled_code):
    # for subroutine declaration
    global indexOf
    global symbol_table
    global static_count
    global field_count
    global subroutine_symbols
    global argument_count
    global local_count
    global subroutine_total
    global currentSubroutineName
    global currentSubroutineType

    indexOf += 1
    initialize_subroutine_symbols()
    currentSubroutineType = token_syntax[indexOf][1]
    indexOf += 2
    currentSubroutineName = token_syntax[indexOf][1]
    indexOf += 1
    if currentSubroutineType == 'method':
        subroutine_symbols['this'] = ['argument', currentClassName, 0]
        subroutine_total += 1
        argument_count += 1
    indexOf += 1
    writeParameterList(token_syntax, compiled_code)
    indexOf += 2
    writeSubroutineBody(token_syntax, compiled_code)
    indexOf += 1


def writeSubroutineBody(token_syntax, compiled_code):
    global indexOf
    global currentSubroutineName
    global local_count
    global currentClassName
    indexOf += 2
    # symbols
    while (token_syntax[indexOf][0] == '<varDec>'):
        writeVarDec(token_syntax)
        indexOf += 1
    compiled_code.append("function " + currentClassName + "." +
                         currentSubroutineName + " " + str(local_count) + "\n")
    if currentSubroutineType == 'constructor':
        compiled_code.append("push constant " + str(field_count) + "\n")
        compiled_code.append("call Memory.alloc 1\npop pointer 0\n")
    if currentSubroutineType == 'method':
        compiled_code.append("push argument 0\npop pointer 0\n")
    writeStatements(token_syntax, compiled_code)
    indexOf += 2


def writeParameterList(token_syntax, compiled_code):
    global indexOf
    global subroutine_symbols
    global argument_count
    global local_count
    global subroutine_total
    indexOf += 1
    if token_syntax[indexOf][0] != '</parameterList>':
        if token_syntax[indexOf][1] in types:
            type = token_syntax[indexOf][1]
            indexOf += 1
        elif token_syntax[indexOf][0][1:-1] == 'identifier':
            type = token_syntax[indexOf][1]
            indexOf += 1
        variable = token_syntax[indexOf][1]
        indexOf += 1
        subroutine_symbols[variable] = ['argument', type, argument_count]
        argument_count += 1
        subroutine_total += 1
        while (token_syntax[indexOf][0] == '<symbol>' and token_syntax[indexOf][1] == ','):
            indexOf += 1
            if token_syntax[indexOf][1] in types:
                type = token_syntax[indexOf][1]
                indexOf += 1
            elif token_syntax[indexOf][0][1:-1] == 'identifier':
                type = token_syntax[indexOf][1]
                indexOf += 1
            variable = token_syntax[indexOf][1]
            indexOf += 1
            subroutine_symbols[variable] = ['argument', type, argument_count]
            argument_count += 1
            subroutine_total += 1


def writeExpression(token_syntax, compiled_code):
    global indexOf
    indexOf += 1
    if token_syntax[indexOf][0][1:-1] == 'term':
        writeTerm(token_syntax, compiled_code)
        indexOf += 1
        while token_syntax[indexOf][0] == '<symbol>' and token_syntax[indexOf][1] in op:
            writeop = token_syntax[indexOf][1]
            indexOf += 1
            writeTerm(token_syntax, compiled_code)
            indexOf += 1
            compiled_code.append(operations[writeop])


def writeExpressionList(token_syntax, compiled_code):
    global indexOf
    nP = 0
    indexOf += 1
    if token_syntax[indexOf][0] != '</expressionList>':
        writeExpression(token_syntax, compiled_code)
        nP += 1
        indexOf += 1
        while (token_syntax[indexOf][0] == '<symbol>' and token_syntax[indexOf][1] == ','):
            indexOf += 1
            writeExpression(token_syntax, compiled_code)
            nP += 1
            indexOf += 1
    return nP


"""
if number n then output ‘‘push n’’
if variable v then output ‘‘push v’’
if (exp1 op exp2) then write(exp1), write(exp2), output ‘‘op’’
if op(exp1) then write(exp1), output ‘‘op’’
if f(exp1 . . . expN) then write(exp1), . . ., write(expN), output ‘‘call f’’
"""


def writeTerm(token_syntax, compiled_code):
    global indexOf
    indexOf += 1
    # if unary
    if token_syntax[indexOf][1] in unaryoperationserations:
        writeop = token_syntax[indexOf][1]
        indexOf += 1
        writeTerm(token_syntax, compiled_code)
        indexOf += 1
        compiled_code.append(unary_code[writeop])
    # else depending on term
    elif token_syntax[indexOf][1] == '(':
        indexOf += 1
        writeExpression(token_syntax, compiled_code)
        indexOf += 2
    elif token_syntax[indexOf][0][1:-1] == 'integerConstant':
        compiled_code.append("push constant " +
                             token_syntax[indexOf][1] + "\n")
        indexOf += 1
    elif token_syntax[indexOf][1] in keywordConstant:
        valu = token_syntax[indexOf][1]
        if valu == 'true':
            compiled_code.append("push constant 0\nnot\n")
        elif valu == 'false' or valu == 'null':
            compiled_code.append("push constant 0\n")
        else:
            compiled_code.append("push pointer 0\n")
        indexOf += 1
    elif token_syntax[indexOf][0][1:-1] == 'identifier':
        variable = token_syntax[indexOf][1]
        id1 = variable
        a = (len(token_syntax[indexOf+1]) >
             1 and token_syntax[indexOf+1][1] not in ['(', '[', '.'])
        b = len(token_syntax[indexOf+1]) <= 1
        if a or b:
            if variable in subroutine_symbols:
                kind = subroutine_symbols[id1][0]
                type = str(subroutine_symbols[id1][2])
                if kind == "field":
                    kind = "this"
                compiled_code.append("push " + kind + " " + type + "\n")
            elif variable in symbol_table:
                kind = symbol_table[id1][0]
                type = str(symbol_table[id1][2])
                if kind == "field":
                    kind = "this"
                compiled_code.append("push " + kind + " " + type + "\n")
            indexOf += 1
        elif token_syntax[indexOf+1][1] == '[':
            indexOf += 2
            writeExpression(token_syntax, compiled_code)
            indexOf += 2
            if variable in subroutine_symbols:
                kind = subroutine_symbols[id1][0]
                type = subroutine_symbols[id1][1]
                ind = str(subroutine_symbols[id1][2])
                if kind == "field":
                    kind = "this"
                compiled_code.append("push " + kind + " " + ind + "\n")
            elif variable in symbol_table:
                kind = symbol_table[id1][0]
                type = symbol_table[id1][1]
                ind = str(symbol_table[id1][2])
                if kind == "field":
                    kind = "this"
                compiled_code.append("push " + kind + " " + ind + "\n")
            compiled_code.append("add\npop pointer 1\npush that 0\n")
        else:
            indexOf += 1
            if token_syntax[indexOf][1] == '.':
                indexOf += 1
                id2 = token_syntax[indexOf][1]
                indexOf += 1
                type = ""
                if id1 in subroutine_symbols:
                    kind = subroutine_symbols[id1][0]
                    type = subroutine_symbols[id1][1]
                    ind = str(subroutine_symbols[id1][2])
                    if kind == "field":
                        kind = "this"
                    compiled_code.append("push " + kind + " " + ind + "\n")
                elif id1 in symbol_table:
                    kind = symbol_table[id1][0]
                    type = symbol_table[id1][1]
                    ind = str(symbol_table[id1][2])
                    if kind == "field":
                        kind = "this"
                    compiled_code.append("push " + kind + " " + ind + "\n")
                indexOf += 1
                nP = writeExpressionList(token_syntax, compiled_code)
                indexOf += 2
                if id1 in symbol_table or id1 in subroutine_symbols:
                    compiled_code.append("call " + type + "." +
                                         id2 + " " + str(nP+1) + "\n")
                else:
                    compiled_code.append("call " + id1 + "." +
                                         id2 + " " + str(nP) + "\n")
            else:
                compiled_code.append("push pointer 0\n")
                indexOf += 1
                nP = writeExpressionList(token_syntax, compiled_code)
                indexOf += 2
                compiled_code.append("call " + currentClassName +
                                     "." + id1 + " " + str(nP+1) + "\n")

    elif token_syntax[indexOf][0][1:-1] == 'stringConstant':
        s = ' '.join(token_syntax[indexOf][1:-1])
        s += " "
        indexOf += 1
        compiled_code.append("push constant " +
                             str(len(s)) + "\ncall String.new 1\n")
        for i in s:
            compiled_code.append("push constant " + str(ord(i)) +
                                 "\ncall String.appendChar 2\n")
    else:
        pass


# function lookup table
f = {"letStatement": writeLet, "ifStatement": writeIf, "doStatement": writeDo,
     "whileStatement": writeWhile, "returnStatement": writeReturn}
