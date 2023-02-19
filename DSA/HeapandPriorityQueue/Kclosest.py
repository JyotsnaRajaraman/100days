# Question
# Given an array of points where
# points[i] = [xi, yi] represents a point on the X-Y plane and an integer k
# Return the k closest points to the origin (0, 0).


def kClosest(points, k):
    return sorted(points, key=lambda point: point[0]**2 + point[1]**2)[:k]
