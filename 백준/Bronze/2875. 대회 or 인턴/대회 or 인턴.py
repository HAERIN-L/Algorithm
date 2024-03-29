n, m, k = map(int, input().split())

# 최대 팀 수
max_team = min(n//2, m)

# 남은 인턴 수
k -= n -max_team *2 + m -max_team

# 추가 팀 생성
while k >0:
    max_team -= 1
    k -= 3
    
print(max_team)