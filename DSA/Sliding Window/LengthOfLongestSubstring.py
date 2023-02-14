# Question
# Given a string s
# # Find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    longest = 0
    letters = set()
    while end < len(s):
        if s[end] not in letters:
            letters.add(s[end])
            longest = max(longest, len(letters))
            end += 1
        else:
            letters.remove(s[start])
            start += 1
    return longest
