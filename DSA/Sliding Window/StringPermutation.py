# Question
# Given two strings s1 and s2
# Return true if s2 contains a permutation of s1, or false otherwise.

def checkInclusion(s1, s2):
    s1 = sorted(s1)
    for i in range(len(s1), len(s2)+1):
        s2sub = sorted(s2[(i-len(s1)): i])
        if s1 == s2sub:
            return True
    return False


print(checkInclusion(s1="adc", s2="dcda"))
