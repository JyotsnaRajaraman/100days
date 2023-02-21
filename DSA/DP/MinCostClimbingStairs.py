# Question
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

def minCostClimbingStairs(cost):
    n = len(cost)
    mincosts = [0]*n
    mincosts[0] = cost[0]
    mincosts[1] = cost[1]
    i = 2
    while (i <= n-1):
        mincosts[i] = min(mincosts[i-1], mincosts[i-2]) + cost[i]
        i += 1
    return min(mincosts[n-1], mincosts[n-2])
