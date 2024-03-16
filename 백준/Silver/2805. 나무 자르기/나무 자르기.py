import sys

# 입력값을 빠르게 받기 위한 설정
input = sys.stdin.readline

# 나무의 개수와 필요한 나무의 길이 입력 받기
n, k = map(int, input().split())

# 나무 길이 리스트 입력 받기
trees = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 1, max(trees)

# 이진 탐색 수행
while start <= end:
    mid = (start + end) // 2
    total = sum([tree - mid if tree > mid else 0 for tree in trees])
    
    # 필요한 나무 길이보다 총 길이가 크거나 같으면 덜 자르기
    if total >= k:
        start = mid + 1
    else: # 필요한 나무 길이보다 총 길이가 작으면 더 많이 자르기
        end = mid - 1

# 최대 높이 출력
print(end)
