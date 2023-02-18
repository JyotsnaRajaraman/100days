# Question
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

def combinationSum(candidates, target):
    res = [[num] + sublist for num in candidates for sublist in self.combinationSum(
        candidates, target - num) if num <= (sublist[0] if sublist else target)] if target > 0 else [[]]
    return res
