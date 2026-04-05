class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        answer = 0

        def dfs(r, c):
            gold = grid[r][c]
            grid[r][c] = 0 

            max_next = 0
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    max_next = max(max_next, dfs(nr, nc))

            grid[r][c] = gold
            return gold + max_next

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    answer = max(answer, dfs(i, j))

        return answer