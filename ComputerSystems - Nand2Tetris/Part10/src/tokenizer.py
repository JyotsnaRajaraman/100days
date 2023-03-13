# To find token type of expression
def tokenType(exp):
    # it is either a sym, keyword, interger (only numbers), or enclosed in quotes and is a stringconstant
    if exp in ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']:
        return "keyword"
    elif exp in ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']:
        return "symbol"
    elif exp.isnumeric():
        return "integerConstant"
    elif exp[0] == '"':
        return "stringConstant"
    # if none of the above are valid, it must be a variable name (id)
    else:
        return "identifier"

# convert the lines into tokens


def tokenize(lines):
    # tokens begin
    tokens = ["<tokens>\n"]
    for line in lines:
        # since we already inserted spaces between symbols, we can simply sep by space
        line = line.split(" ")
        j = 0
        # each line may have multiple characters
        while j < (len(line)):
            word = line[j]
            # there may be extra spaces/tabs
            word = word.strip()
            if word == "" or word == []:
                j += 1
                continue
            # some string constants are multiple words, so we need to check until " comes again
            if word[0] == '"' and word[-1] != '"':
                j += 1
                while line[j][-1] != '"':
                    word += " " + line[j]
                    j += 1
                word += " " + line[j]
            # find token type
            token = tokenType(word)
            if token == "stringConstant":
                # remove double quotes
                word = word[1:-1]
            # these are special variables
            if word in ["<", ">", "&"]:
                if word == "<":
                    word = "&lt;"
                elif word == ">":
                    word = "&gt;"
                else:
                    word = "&amp;"
            # tokenize
            parsedTokens = "<" + token + "> " + \
                word + " </" + token + ">\n"
            tokens.append(parsedTokens)
            j += 1
    # end the tokens part
    tokens.append("</tokens>")
    return tokens
