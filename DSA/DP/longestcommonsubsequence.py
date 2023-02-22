# Question
# Given two strings text1 and text2
# Return the length of their longest common subsequence.
# If there is no common subsequence, return 0.

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n1, n2 = len(text1), len(text2)
    dp = [[0] * n2 for _ in range(n1)]
    for i in range(n1):
        for j in range(n2):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
            else:
                dp[i][j] = max(dp[i][j-1] if j > 0 else 0,
                               dp[i-1][j] if i > 0 else 0)
    return dp[-1][-1]
