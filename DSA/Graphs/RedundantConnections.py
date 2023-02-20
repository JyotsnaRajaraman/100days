from collections import defaultdict
# Question
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.


def findRedundantConnection(edges):
    def dfs(u, v):
        if u in visited:
            return False
        if u == v:
            return True

        visited.add(u)

        for i in graph[u]:
            if dfs(i, v):
                return True
        return False

    n = len(edges)
    graph = defaultdict(list)

    ans = []
    for u, v in edges:
        visited = set()
        if dfs(u, v):
            ans = [u, v]
        graph[u].append(v)
        graph[v].append(u)
    return ans
