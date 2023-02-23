# Question
# Given a non-empty array of integers nums,
# every element appears twice except for one.
# Find that single one.

def singleNumber(self, nums: List[int]) -> int:
    return (x := 0, [x := x ^ v for v in nums])[-1][-1]
