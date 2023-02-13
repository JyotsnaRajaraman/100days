# Question
# Given an array of strings strs, group the anagrams together.

def groupAnagrams(strs):
    d = {}
    for word in strs:
        key = tuple(sorted(word))
        d[key] = d.get(key, [])+[word]
    return d.values()
