def insert(intervals, newInterval): 
    n = newInterval
    j = intervals
    i = 0
    m = n[0]
    m1 = n[1]
    while i < len(j):
        if n[0] in range(j[i][0], j[i][1]+1) or n[1] in range(j[i][0], j[i][1]+1) or (n[1] >= j[i][1] and n[0] <= j[i][0]):
            if j[i][0] < m:
                m = j[i][0]
            if j[i][1] > m1:
                m1 = j[i][1]
            j.pop(i)
            if i <= 0:
                i = 0
            else:
                i -= 1
        else:
            i += 1
    s1 = [m, m1]
    j.append(s1)
    j.sort()
    return j
