# Question
# Given an integer array nums and an integer k, return the k most frequent elements.

def topKFrequent(nums, k):
    frequency = {}
    for num in nums:
        frequency[num] = 1 + frequency.get(num, 0)
    return (sorted(frequency, key=frequency.get, reverse=True))[:k]
