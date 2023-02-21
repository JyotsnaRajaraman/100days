# Question
# All houses at this place are arranged in a circle.
# Adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into
# Given an integer array nums representing the amount of money of each house
# Return the maximum amount of money you can rob tonight without alerting the police


def rob(nums):
    n = len(nums)
    if n > 1:
        def loot(nums):
            n = len(nums)
            if n <= 1:
                return nums[0]
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
        return max(loot(nums[1:]), loot(nums[:n-1]))
    return nums[0]
