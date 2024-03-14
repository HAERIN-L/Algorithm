import sys

def calc(start, end, arr, n):
    if end - start <= 1:
        return start
        
    mid = (start + end) // 2 # mid라는 길이라면 전체 개수가 몇 개 나오는지 구해야해서 rst 사용
    rst = 0
    
    for item in arr:
        rst += (item // mid)
    if rst < n:
        return calc(start, mid, arr, n)
    else: # rst >= n
        return calc(mid, end, arr, n)

def solve():
    k, n = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    big = 0
    for _ in range(k):
        x = int(sys.stdin.readline().rstrip())
        big = max(big, x)
        arr.append(x)
    print(calc(1, big+1, arr, n)) # big+1 전까지

solve()
