# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead
# And she will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return .
# Return the minimum integer k such that she can eat all the bananas within h hour

from math import ceil


def minEatingSpeed(piles, h):
    lptr = 1
    rptr = max(piles)
    answer = rptr
    while lptr <= rptr:
        midspeed = (lptr+rptr)//2
        hours = 0
        for pile in piles:
            hours += ceil(pile/midspeed)
        if hours <= h:
            answer = min(answer, midspeed)
            rptr = midspeed - 1
        else:
            lptr = midspeed + 1
    return answer
