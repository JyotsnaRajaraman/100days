# Question
# Given an integer array nums representing the amount of money of each house
# Return the maximum amount of money you can rob tonight without alerting the police

def rob(nums):
    n = len(nums)
    if n > 1:
        maxloot = [0]*n
        maxloot[0] = nums[0]
        house0 = False
        if nums[1] < nums[0]:
            maxloot[1] = nums[0]
            house0 = True
        else:
            maxloot[1] = nums[1]
        i = 2
        while i < n:
            maxloot[i] = max(maxloot[i-2]+nums[i], maxloot[i-1])
            i += 1
        return max(maxloot[n-1], maxloot[n-2])
    return nums[0]
