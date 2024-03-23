from collections import deque

# 미로 크기 입력
n, m = map(int, input().split())
# 미로 입력
maze = [list(map(int, list(input()))) for _ in range(n)]

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 범위 안에 있고, 이동 가능한 칸일 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 이동한 칸에 현재까지의 이동 횟수 +1
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # (N, M) 위치의 이동 횟수 반환
    return maze[n-1][m-1]

# BFS 탐색 시작
print(bfs(0, 0))