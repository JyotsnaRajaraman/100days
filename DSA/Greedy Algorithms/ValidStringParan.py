def checkValidString(self, s: str) -> bool:
    lefts = 0
    rights = 0
    for c in s:
        if c == "(":
            lefts = lefts + 1
            rights = rights + 1
        elif c == ")":
            lefts = lefts - 1
            rights = rights - 1
        else:
            lefts = lefts - 1
            rights = rights + 1
        if rights < 0:
            return False
        if lefts < 0:
            lefts = 0
    return lefts == 0
