# Question
# Given the array nums after the possible rotation and an integer target
# Return the index of target if it is in nums, or -1 if it is not in nums.

def search(nums, target):
    lptr = 0
    rptr = len(nums)-1
    while lptr <= rptr:
        mid = (lptr+rptr)//2
        if nums[mid] == target:
            return mid
        if nums[lptr] <= nums[mid]:
            if target >= nums[lptr] and target <= nums[mid]:
                rptr = mid-1
            else:
                lptr = mid+1
        else:
            if target > nums[mid] and target <= nums[rptr]:
                lptr = mid+1
            else:
                rptr = mid-1
    return -1
