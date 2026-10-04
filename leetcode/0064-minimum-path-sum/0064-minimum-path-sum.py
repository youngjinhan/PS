class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        s = [[0 for col in range(n)] for row in range(m)]
        s[0][0] = grid[0][0]

        for i in range(1, n):
            s[0][i] = s[0][i-1] + grid[0][i]

        for i in range(1, m):
            s[i][0] = s[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                s[i][j] = grid[i][j] + min(s[i-1][j], s[i][j-1])

        return s[m-1][n-1]
