# Question
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water)
# return the number of islands.

def numIslands(self, grid: List[List[str]]) -> int:
    islands = 0

    def dfs(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "2"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(r, c)
                islands += 1
    return islands
