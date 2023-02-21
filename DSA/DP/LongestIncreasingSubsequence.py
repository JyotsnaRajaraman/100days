# Question
# Given an integer array nums,
# return the length of the longest strictly increasing subsequence

def lengthOfLIS(nums):
    n = len(nums)
    longestSub = [1]*n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                longestSub[i] = max(longestSub[i], 1+longestSub[j])
    return max(longestSub)
