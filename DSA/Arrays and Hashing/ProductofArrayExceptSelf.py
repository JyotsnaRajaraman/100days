# Question
# Given an integer array nums
# Return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i]

def productExceptSelf(nums):
    prefix = [1]*len(nums)
    suffix = [1]*len(nums)
    answer = [1]*len(nums)
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]
    for i in range(len(nums)-2, -1, -1):
        suffix[i] = suffix[i+1]*nums[i+1]
    for i in range(len(nums)):
        answer[i] *= prefix[i] * suffix[i]

    return answer
