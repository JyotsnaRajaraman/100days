# Question
# Given the sorted rotated array nums of unique elements
# Return the minimum element of this array.
# Algorithm must run in O(log n) time.

def findMin(nums):
    rptr = len(nums) - 1
    lptr = 0
    while rptr - 1 > lptr:
        mid = (lptr + rptr)//2
        if nums[lptr] > nums[mid]:
            rptr = mid
        else:
            lptr = mid

    if nums[rptr] > nums[lptr]:
        return nums[0]
    return nums[rptr]
