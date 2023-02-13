# Question
# Given two strings s and t
# Return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    sletters = {}
    for l in s:
        if l not in sletters:
            sletters[l] = 1
        else:
            sletters[l] = sletters.get(l) + 1
    # check if t is satisfied
    for i in range(len(t)):
        l = t[i]
        if l not in sletters:
            return False
        if sletters.get(l) <= 0:
            return False
        else:
            sletters[l] = sletters.get(l) - 1

    for l in sletters:
        if sletters.get(l) > 0:
            return False
    return True
