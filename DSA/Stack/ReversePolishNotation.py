# Question
# You are given an array of strings tokens
# the input represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression and return an integer that represents it's value

def evalRPN(tokens):
    workingstack = []
    for n in tokens:
        if n.isdigit() or (len(n) > 1 and n[1:].isdigit()):
            workingstack.append(int(n))
        elif n == "+":
            b = workingstack.pop()
            a = workingstack.pop()
            workingstack.append(a+b)
        elif n == "-":
            b = workingstack.pop()
            a = workingstack.pop()
            workingstack.append(a-b)
        elif n == "*":
            b = workingstack.pop()
            a = workingstack.pop()
            workingstack.append(a*b)
        elif n == "/":
            b = workingstack.pop()
            a = workingstack.pop()
            workingstack.append(int(a/b))
    return workingstack[0]


print(evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
