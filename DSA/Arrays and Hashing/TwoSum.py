# Question
# Given an array of integers nums and an integer target
# Return indices of the two numbers such that they add up to target


def twoSum(nums, target):
    numssofar = {}
    for index, num in enumerate(nums):
        if num not in numssofar:
            numssofar[target-num] = index
        else:
            out = [index]
            out.append(numssofar.get(num))
    return out
