# Question
# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
from sortedcontainers import SortedList


class KthLargest:

    def __init__(self, k: int, nums):
        self.numlst = SortedList(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.numlst.add(val)
        return self.numlst[-self.k]
