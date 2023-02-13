# Question
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order
# Find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

def twoSum(numbers, target):
    ptr1 = 0
    ptr2 = len(numbers)-1
    while ptr1 != ptr2:
        current = numbers[ptr1] + numbers[ptr2]
        if current == target:
            return [ptr1+1, ptr2+1]
        elif current > target:
            ptr2 -= 1
        else:
            ptr1 += 1
