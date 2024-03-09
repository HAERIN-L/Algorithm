from collections import deque 

def solution(bridge_length, weight, truck_weights):
    # 대기 중인 트럭을 deque 자료구조로 변환
    truck_weights = deque(truck_weights)
    # 다리를 표현하는 deque을 생성하고, 처음에는 0으로 초기화
    bridge = deque([0 for i in range(bridge_length)])
    # 경과 시간을 저장하는 변수
    time = 0
    # 다리를 건너고 있는 트럭들의 무게를 저장하는 변수
    b_weight = 0
    
    # 다리에 트럭이 있는 동안에 반복
    while len(bridge) != 0:
        # 다리를 건넌 트럭을 deque에서 제거하고 그 무게를 다리 무게에서 빼줌
        out = bridge.popleft()
        if out != 0:  # 트럭이 다리를 건너는 경우에만 무게 갱신
            b_weight -= out
        # 시간을 1초 증가시킴
        time += 1
        
        # 대기 중인 트럭이 있으면 다리에 진입 가능 여부를 판단
        if truck_weights:
            if b_weight + truck_weights[0] <= weight: # 현재 다리에 진입 가능한 경우
                # 대기 중인 트럭을 다리로 이동시키고, 다리 무게와 다리에 추가
                truck = truck_weights.popleft()
                b_weight += truck
                bridge.append(truck)
            else: # 현재 다리에 진입 불가능한 경우
                # 다음 트럭이 못지나가므로, 0을 다리에 추가
                bridge.append(0)
    
    # 모든 트럭이 다리를 건넌 후에 경과된 시간을 반환
    return time
