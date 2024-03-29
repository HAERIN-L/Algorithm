n = int(input())
cards = list(map(int, input().split()))

# 가장 등급 높은 카드 찾음
max_card = max(cards)

# 모든 카드 합치는 비용 계산 
total = 0
for card in cards:
    total += card
    
# 가장 높은 등급 카드를 제외한 나머지 카드를 합치는 비용 계산
total -= max_card

print(total + max_card*(n-1))