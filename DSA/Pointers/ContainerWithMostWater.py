# Question
# You are given an integer array height of length n.
# There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Return the maximum amount of water a container can store.

def maxArea(height):
    #area = width * height
    # going from the middle, we compare the max areas
    # max area of full length * min height vs left half vs right half
    lptr = 0
    rptr = len(height)-1
    answer = 0
    while lptr < rptr:
        midwidth = rptr-lptr
        midheight = min(height[lptr], height[rptr])
        area = midwidth*midheight
        answer = max(answer, area)
        if height[lptr] >= height[rptr]:
            rptr -= 1
        else:
            lptr += 1
    return answer


print(maxArea([1, 1]))
