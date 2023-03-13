from hashlib import new
from lookup import destdict, compdict, jmpdict, symbols

# dictionary lookups for each code part


def dest(destination):
    return destdict.get(destination)


def comp(computation):
    return compdict.get(computation)


def jmp(jump):
    return jmpdict.get(jump)


def removelabels(lines):
    pass1 = []
    linecount = 0
    for line in lines:
        # assign label to line numbers and add to symbol table and remove that line
        if line[0] == "(":
            newline = line.replace("(", "")
            newline = newline.replace(")", "")
            newline = newline.replace("\n", "")
            symbols[newline] = "{:0>16b}".format(linecount)
        else:
            pass1.append(line)
            linecount += 1
    return pass1
    # return [i for i in list(map(str.lstrip, lines)) if i]


def translate(lines):
    pass2 = []
    nextavailableRAM = 16
    for line in lines:
        # check if A or C command
        # remove newline character if it exists
        if line[-1:] == "\n":
            line = line[:-1]
        if line[0] == "@":
            # check whether variable or number
            tostore = line[1:]
            if tostore.isdigit():
                # convert number to binary
                newline = "{:0>16b}".format(int(tostore))
            else:
                # check whether variable is in the symbols list or not
                if tostore not in symbols:
                    symbols[tostore] = "{:0>16b}".format(nextavailableRAM)
                    nextavailableRAM += 1
                newline = str(symbols.get(tostore)).zfill(16)
            pass2.append(newline + ("\n"))
        else:
            # check if there is a dest or jmp
            equals = line.find("=")
            semicolon = line.find(";")
            if equals != -1:
                x = line[equals+1:]
                newline = "111" + comp(x) + \
                    dest(line[:equals]) + "000"
                pass2.append(newline + ("\n"))
            elif semicolon != -1:
                newline = "111" + comp(line[:semicolon]) + \
                    "000" + jmp(line[semicolon+1:])
                pass2.append(newline + ("\n"))
            else:
                newline = "111" + comp(line) + "000000"
                pass2.append(newline + ("\n"))

    # remove final newline character
    pass2[-1] = pass2[-1][:-1]

    return pass2
