# Question
# Given a string s
# Return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    if len(s) < 2:
        return True
    start = 0
    end = len(s)-1
    while start != end:
        if s[start].isalnum() and s[end].isalnum():
            if s[start] != s[end]:
                return False
            if end-start > 1:
                start += 1
                end -= 1
            else:
                break
        else:
            if s[start].isalnum():
                end -= 1
            else:
                start += 1

    return True
