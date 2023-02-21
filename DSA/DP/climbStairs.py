# Question
# You are climbing a staircase.
# It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


def climbStairs(n: int) -> int:
    waystoclimb = [0]*(n+1)
    waystoclimb[0] = 1
    waystoclimb[1] = 1
    i = 2
    while i <= n:
        waystoclimb[i] = waystoclimb[i-2] + waystoclimb[i-1]
        i += 1
    return waystoclimb[n]
