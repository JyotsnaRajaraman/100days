# Question
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

def searchMatrix(matrix, target):
    m = 0
    answer = False
    while m < len(matrix) and answer == False:
        if matrix[m][-1] >= target:
            for num in matrix[m]:
                if num == target:
                    answer = True
                    break
        m += 1
    return answer
