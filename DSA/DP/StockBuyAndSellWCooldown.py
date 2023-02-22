# Question
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
    n = len(prices)
    dp = [0] * (n+1)
    min_price = prices[0]
    for i in range(1, n+1):
        min_price = min(min_price, prices[i-1]-dp[i-2])
        dp[i] = max(dp[i-1], prices[i-1]-min_price)

    return dp[n]
