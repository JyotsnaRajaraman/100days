# split the token types into categories that need separate compile functions
function_types = {'constructor', 'function', 'method'}
special = {'<', '>', '&', '"'}
types = {'int', 'char', 'boolean'}
function_types = {'constructor', 'function', 'method'}
statements = {'let', 'if', 'while', 'do', 'return'}
op = {'+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '='}
unaryOp = {'-', '~'}
keywordConstant = {'true', 'false', 'null', 'this'}

# compilation engine to compile the whole class


def CompilationEngine(inputlines):
    compiledlines = []
    tokens = []
    for line in inputlines:
        # separate with space we inserted between <>, actual character and </>
        line = line.split()
        # we need to check whether len > 1
        # this is because we have <token> and </token> which actually don't mean anythign in this context
        if (len(line) > 1):
            tokens.append(line)
    if (len(tokens) > 0):
        # all files start with class
        compileClass(tokens, compiledlines)
    return compiledlines


def compileClass(tokens, compiledlines):
    if len(tokens) == 0:
        return
    # append class, classname ...
    # class: 'class' className '{' classVarDec* subroutineDec* '}'
    compiledlines.append("<class>\n")
    compiledlines.append(tokens[0][0]+" "+tokens[0]
                         [1]+" "+tokens[0][2]+"\n")
    compiledlines.append(tokens[1][0]+" "+tokens[1]
                         [1]+" "+tokens[1][2]+"\n")
    compiledlines.append(tokens[2][0]+" "+tokens[2]
                         [1]+" "+tokens[2][2]+"\n")
    # call other parts
    tokens = tokens[3:-1]
    global ind
    ind = 0
    if (len(tokens)) > 0:
        while (tokens[ind][1] == 'static' or tokens[ind][1] == 'field'):
            compiledlines.append("<classVarDec>\n")
            compileClassVarDec(tokens, compiledlines)
            compiledlines.append("</classVarDec>\n")
        if (len(tokens) > ind):
            while len(tokens) > ind and tokens[ind][1] in function_types:
                compiledlines.append("<subroutineDec>\n")
                compilesubroutineDec(tokens, compiledlines)
                compiledlines.append("</subroutineDec>\n")

    compiledlines.append(tokens[-1][0]+" "+tokens[-1]
                         [1]+" "+tokens[-1][2]+"\n")
    compiledlines.append("</class>\n")
    return compiledlines


def compileExpressionList(tokens, compiledlines):
    # always refer to global index since each func has control to parse until needed
    global ind
    # expressionList: (expression (',' expression)* )?
    if tokens[ind][1] != ')':
        compiledlines.append("<expression>\n")
        compileExpression(tokens, compiledlines)
        compiledlines.append("</expression>\n")
        while tokens[ind][1] == ',':
            compiledlines.append(
                tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
            ind += 1
            compiledlines.append("<expression>\n")
            compileExpression(tokens, compiledlines)
            compiledlines.append("</expression>\n")


def compilesubroutineCall(tokens, compiledlines):
    global ind
    # subroutineName '(' expressionList ')' | (className | varName) '.' subroutineName '(' expressionList ')'
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    if tokens[ind][1] == '(':
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append("<expressionList>\n")
        compileExpressionList(tokens, compiledlines)
        compiledlines.append("</expressionList>\n")
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
    elif tokens[ind][1] == '.':
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append("<expressionList>\n")
        compileExpressionList(tokens, compiledlines)
        compiledlines.append("</expressionList>\n")
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1


def compileExpression(tokens, compiledlines):
    global ind
    # term (op term)*
    compileTerm(tokens, compiledlines)
    while (tokens[ind][1] in op):
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compileTerm(tokens, compiledlines)


def compileTerm(tokens, compiledlines):
    global ind

    # term: integerConstant | stringConstant | keywordConstant | varName | varName '[' expression ']' | subroutineCall |'(' expression ')' | unaryOp term
    if ind < len(tokens):
        compiledlines.append("<term>\n")
        if (tokens[ind][1] == '('):
            compiledlines.append(
                tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
            ind += 1
            compiledlines.append("<expression>\n")
            compileExpression(tokens, compiledlines)
            compiledlines.append("</expression>\n")
            compiledlines.append(
                tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
            ind += 1
        else:
            if tokens[ind][0][1:-1] in ['integerConstant']:
                compiledlines.append(
                    tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                ind += 1
            elif tokens[ind][1] in keywordConstant:
                compiledlines.append(
                    tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                ind += 1

            elif tokens[ind][0][1:-1] == 'stringConstant':
                compiledlines.append(' '.join(tokens[ind]))
                compiledlines.append('\n')
                ind += 1
            elif tokens[ind][0][1:-1] == 'identifier':
                if (tokens[ind+1][1] == '(' or tokens[ind+1][1] == '.'):
                    compilesubroutineCall(tokens, compiledlines)
                elif tokens[ind+1][1] == '[':
                    compiledlines.append(
                        tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                    ind += 1
                    compiledlines.append(
                        tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                    ind += 1
                    compiledlines.append("<expression>\n")
                    compileExpression(tokens, compiledlines)
                    compiledlines.append("</expression>\n")
                    compiledlines.append(
                        tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                    ind += 1
                else:
                    compiledlines.append(
                        tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                    ind += 1
            elif tokens[ind][1] in unaryOp:
                compiledlines.append(
                    tokens[ind][0]+" "+tokens[ind][1]+" "+tokens[ind][2]+"\n")
                ind += 1
                compileTerm(tokens, compiledlines)
        compiledlines.append("</term>\n")


def compileLet(tokens, compiledlines):
    global ind
    # letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
    compiledlines.append("<letStatement>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    if tokens[ind][1] == '[':
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append("<expression>\n")
        compileExpression(tokens, compiledlines)
        compiledlines.append("</expression>\n")
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<expression>\n")
    compileExpression(tokens, compiledlines)
    compiledlines.append("</expression>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("</letStatement>\n")


def compileIf(tokens, compiledlines):
    global ind

    # ifStatement: 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
    compiledlines.append("<ifStatement>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<expression>\n")
    compileExpression(tokens, compiledlines)
    compiledlines.append("</expression>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<statements>\n")
    compileStatements(tokens, compiledlines)
    compiledlines.append("</statements>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    if (tokens[ind][1] == 'else'):
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append("<statements>\n")
        compileStatements(tokens, compiledlines)
        compiledlines.append("</statements>\n")
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
    compiledlines.append("</ifStatement>\n")


def compileDo(tokens, compiledlines):
    global ind
    # doStatement: 'do' subroutineCall ';'
    compiledlines.append("<doStatement>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compilesubroutineCall(tokens, compiledlines)
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("</doStatement>\n")


def compileWhile(tokens, compiledlines):
    global ind
    # whileStatement: 'while' '(' expression ')' '{' statements '}'
    compiledlines.append("<whileStatement>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<expression>\n")
    compileExpression(tokens, compiledlines)
    compiledlines.append("</expression>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<statements>\n")
    compileStatements(tokens, compiledlines)
    compiledlines.append("</statements>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("</whileStatement>\n")


def compileReturn(tokens, compiledlines):
    # ReturnStatement 'return' expression? ';'
    global ind
    compiledlines.append("<returnStatement>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    if (tokens[ind][1] != ';'):
        compiledlines.append("<expression>\n")
        compileExpression(tokens, compiledlines)
        compiledlines.append("</expression>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("</returnStatement>\n")


def compileStatements(tokens, compiledlines):
    global ind
    # statement*
    while (tokens[ind][1] != '}'):
        funclookup[tokens[ind][1]](tokens, compiledlines)


def compileparameterList(tokens, compiledlines):
    global ind
    # ((type varName) (',' type varName)*)?
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    while (tokens[ind][1] == ','):
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1


def compilesubroutineBody(tokens, compiledlines):
    global ind
    # subroutineBody: '{' varDec* statements '}'
    if (len(tokens) > ind):
        while tokens[ind][1] == 'var':
            compiledlines.append("<varDec>\n")
            compilevarDec(tokens, compiledlines)
            compiledlines.append("</varDec>\n")
        compiledlines.append("<statements>\n")
        if (tokens[ind][1] != '}'):
            compileStatements(tokens, compiledlines)
        compiledlines.append("</statements>\n")


def compilevarDec(tokens, compiledlines):
    global ind
    # varDec: 'var' type varName (',' varName)* ';'
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    while (tokens[ind][1] == ','):
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1


def compileClassVarDec(tokens, compiledlines):
    global ind
    # classVarDec: ('static' | 'field') type varName (',' varName)* ';'
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    while (tokens[ind][1] == ','):
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
        compiledlines.append(tokens[ind][0]+" " +
                             tokens[ind][1]+" "+tokens[ind][2]+"\n")
        ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1


def compilesubroutineDec(tokens, compiledlines):
    global ind
    # ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<parameterList>\n")
    if tokens[ind][1] in types:
        compileparameterList(tokens, compiledlines)
    compiledlines.append("</parameterList>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("<subroutineBody>\n")
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    if tokens[ind][1] != '}':
        compilesubroutineBody(tokens, compiledlines)
    compiledlines.append(tokens[ind][0]+" " +
                         tokens[ind][1]+" "+tokens[ind][2]+"\n")
    ind += 1
    compiledlines.append("</subroutineBody>\n")


# hashtable to refer to functions
funclookup = {"while": compileWhile, "return": compileReturn,
              "let": compileLet, "if": compileIf, "do": compileDo}
