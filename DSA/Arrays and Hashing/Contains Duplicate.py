# Question
# Given an integer array nums
# Return true if any value appears at least twice in the array
# Return false if every element is distinct.

def containsDuplicate(nums):
    numsset = set()
    for num in nums:
        if num not in numsset:
            numsset.add(num)
        else:
            return True
    return False
