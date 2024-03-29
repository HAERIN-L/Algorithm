n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 최소한 동전 개수 계산
count = 0

for coin in sorted(coins, reverse=True):
    count += k// coin
    k %= coin
    
print(count)