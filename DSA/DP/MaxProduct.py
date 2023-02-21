# Question
# Given an integer array nums, find a subarray that has the largest product
# Return the product.

def maxProduct(nums):
    prod = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        prod[i] *= prod[i - 1] or 1
    return max(nums + prod)
