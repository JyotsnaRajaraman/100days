# Question
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums)[-k]
