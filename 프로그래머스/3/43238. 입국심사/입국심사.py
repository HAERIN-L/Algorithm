def solution(n, times):
    answer = 0
    
    left, right = 1, max(times) *n # 가능한 심사 시간의 최소값과 최대값 설정
    
    while left <= right:
        mid = (left + right) //2  # 중간값으로 심사 시간 설정
        
        humans = 0
        
        for time in times:
            humans += mid //time # 각 심사관별로 주어진 시간 동안 심사할 수 있는 사람 수
            
            if humans >= n: #필요한 사람 수를 충족하면 반복 끝냄
                break
        if humans >= n: # 모든 사람을 심사O --> 시간 줄여봄
            answer = mid
            right = mid -1
        else: # 모든 사람 심사 x --> 시간 늘려봄
            left = mid+1 

    return answer