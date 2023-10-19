from collections import deque

n, m = map(int, input().split())

def bfs(x, y):
    global cnt, square
    q = deque([(x, y)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    square_tmp = 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == 0 or visited[x][y]:
            continue
        visited[x][y] = True
        square_tmp += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append((nx, ny))

    if square_tmp > 0:
        cnt += 1
        square = max(square, square_tmp)

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
square = 0
for i in range(n):
    for j in range(m):
        bfs(i, j)

print(cnt, square, sep= '\n')
