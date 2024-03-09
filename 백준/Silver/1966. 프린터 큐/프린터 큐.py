from collections import deque

def p_order(documents, target_idx):
    queue = deque(enumerate(documents)) # 문서의 (순서, 중요도) 튜플을 큐에 추가함
    
    order = 0
    
    while queue:
        current_doc = queue.popleft() # 큐에서 첫 번째 문서를 가져옴
        if any(current_doc[1] < doc[1] for doc in queue): # 현재 문서의 중요도보다 높은 중요도를 가진 문서가 큐에 있는지 확인
            queue.append(current_doc) # 있다면 현재 문서를 큐의 맨 뒤로 보냄
        else:
            order += 1
            if current_doc[0] == target_idx: # 원하는 문서 순서인지 확인
                return order
    return -1 # 문제있으면 -1 반환

n = int(input())

for _ in range(n):
    _, m = map(int, input().split()) # 첫 번째 변수는 무시하고, 두 번째 변수는 m에 할당
    documents = list(map(int, input().split()))
    print(p_order(documents, m))
