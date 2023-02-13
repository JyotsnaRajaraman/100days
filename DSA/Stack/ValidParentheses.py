# Question
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# Determine if the input string is valid.

def isValid(s):
    if len(s) % 2 != 0:
        return False
    pstack = []
    pdict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for p in s:
        if p in ('(', '{', '['):
            pstack.append(p)
        else:
            if len(pstack) > 0:
                if pstack.pop() != pdict.get(p):
                    return False
            else:
                return False
    return len(pstack) == 0
