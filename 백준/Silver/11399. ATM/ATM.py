n = int(input())
t = list(map(int, input().split()))

# t(시간) 오름차순 정렬 
t.sort()

# 각 사람 돈 인출하는데 걸리는 총 시간 최솟값
total_t =0
wait_t =0

for time in t:
    wait_t += time
    total_t += wait_t
    
print(total_t)