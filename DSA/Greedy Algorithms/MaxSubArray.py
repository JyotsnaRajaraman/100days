def maxSubArray(nums):
    maxsum = nums[0]
    total = 0
    for n in nums:
        total += n
        maxsum = max(maxsum, total)
        if total < 0:
            total = 0
    return maxsum
