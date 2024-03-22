from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)