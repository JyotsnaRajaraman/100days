# Question
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order


def subsets(nums):
    nums.sort()
    return [[]] + [sub+[nums[i]] for i in range(len(nums)) for sub in self.subsets(nums[:i])]
