# Question
# Given an integer array nums
# Return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

from itertools import combinations


def threeSum(nums):
    # similar to two sum, except target is the negative of existing array elements
    # we can solve in O(n^2) by splitting the array into positive, neg and zeroes
    if len(nums) < 3:
        return []

    res = set()

    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    negative = set(n)
    positive = set(p)

    if z:
        if len(z) >= 3:
            res.add((0, 0, 0))

        for num in positive:
            if -1 * num in negative:
                res.add((-1 * num, 0, num))

    for x, y in combinations(n, 2):
        target = -1 * (x + y)
        if target in positive:
            res.add(tuple(sorted([x, y, target])))

    for x, y in combinations(p, 2):
        target = -1 * (x + y)
        if target in negative:
            res.add(tuple(sorted([x, y, target])))

    return [list(x) for x in res]
