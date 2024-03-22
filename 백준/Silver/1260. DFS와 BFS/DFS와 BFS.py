from collections import deque

# DFS 함수 정의
def dfs(edges, v, visited):
    visited[v] = True  # 방문한 정점 표시
    print(v, end=' ')  # 방문한 정점 출력
    for e in edges[v]:  # 해당 정점과 연결된 모든 정점에 대해
        if not visited[e]:  # 아직 방문하지 않은 정점이라면
            dfs(edges, e, visited)  # 해당 정점에 대해 DFS 수행
            
# BFS 함수 정의
def bfs(edges, v, visited):
    queue = deque([v])  # 큐에 시작 정점을 넣음
    visited[v] = True  # 방문한 정점 표시
    while queue:  # 큐가 빌 때까지
        now = queue.popleft()  # 큐에서 정점을 하나 꺼냄
        print(now, end=' ')  # 꺼낸 정점 출력
        
        for e in edges[now]:  # 꺼낸 정점과 연결된 모든 정점에 대해
            if not visited[e]:  # 아직 방문하지 않은 정점이라면
                queue.append(e)  # 큐에 추가
                visited[e] = True  # 방문한 정점 표시
                
n, m, v = map(int, input().split())  # 정점의 개수, 간선의 개수, 시작 정점 입력 받음
edges =[[] for _ in range(n+1)]  # 간선 정보를 저장할 리스트 초기화

for _ in range(m):  # 간선의 개수만큼
    a, b = map(int, input().split())  # 간선 정보 입력 받음
    edges[a].append(b)  # 간선 정보 저장
    edges[b].append(a)  # 간선 정보 저장
    
for i in range(1, n+1):  # 모든 정점에 대해
    edges[i].sort()  # 간선 정보 정렬
    
visited = [False] * (n+1)  # 방문 정보를 저장할 리스트 초기화
dfs(edges, v, visited)
print() 

visited = [False] * (n+1)
bfs(edges, v, visited)
