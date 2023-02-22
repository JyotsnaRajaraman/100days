# Question
# There is a robot on an m x n grid. The robot is initially located at the top-left corner
# The robot tries to move to the bottom-right corner
# The robot can only move either down or right at any point in time.
# Given the two integers m and n,
# Return the number of possible unique paths that the robot can take

def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1]*n for i in range(2)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i & 1][j] = dp[(i-1) & 1][j] + dp[i & 1][j-1]
    return dp[(m-1) & 1][-1]
