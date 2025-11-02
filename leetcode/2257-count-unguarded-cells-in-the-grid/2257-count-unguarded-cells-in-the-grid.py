class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[0 for col in range(n)] for row in range(m)]

        for x, y in walls:
            cells[x][y] = -1

        for x, y in guards:
            cells[x][y] = 2

        # for x, y in guards:
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx, ny + dy

                    if 0 <= nx < m and 0 <= ny < n and 0 <= cells[nx][ny] <= 1:
                        cells[nx][ny] = 1
                    else:
                        break

        ans = 0
        for i in range(m):
            for j in range(n):
                if cells[i][j] == 0:
                    ans += 1

        return ans