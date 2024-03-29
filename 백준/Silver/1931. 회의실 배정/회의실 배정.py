n = int(input())

meeting = []
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))
    
# 회의 끝나는 시간 기준으로 오름차순 정렬
meeting.sort(key = lambda x: (x[1], x[0]))

# 가능한 많은 회의 선택
select_meeting =[]
end_time = 0

for meet in meeting:
    start, end = meet
    if start >= end_time:
        select_meeting.append(meet)
        end_time = end
        
print(len(select_meeting))