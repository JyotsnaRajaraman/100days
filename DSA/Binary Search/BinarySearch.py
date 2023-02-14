# Question
# Given an array of integers nums which is sorted in ascending order,
# And an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

def search(nums, target):
    lower = 0
    upper = len(nums)-1
    while lower < upper:
        mid = int((lower + upper)/2)
        if target == nums[mid]:
            return mid
        elif (target > nums[mid]):
            lower = mid+1
        else:
            upper = mid-1
    if nums[lower] == target:
        return lower
    else:
        return -1
