from collections import deque

def solve(n, k): # n: 수빈이의 현재 위치, k: 동생의 위치
    time = [0] * (200001)
    q = deque([n]) # 방문할 위치를 저장하는 큐
    time[n] = 0 # 각 위치에 도달하는데 걸리는 시간

    while q:
        now = q.popleft()
        if now == k:
            print(time[k])
            return

        if abs(k - now) > abs(k - 2 * now) and time[2 * now] == 0:
            q.append(2 * now)
            time[2 * now] = time[now] + 1

        if now + 1 <= 100000 and time[now + 1] == 0:
            q.append(now + 1)
            time[now + 1] = time[now] + 1

        if now - 1 >= 0 and time[now - 1] == 0:
            q.append(now - 1)
            time[now - 1] = time[now] + 1

n, k = map(int, input().split())
solve(n, k)