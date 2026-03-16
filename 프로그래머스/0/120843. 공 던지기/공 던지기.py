def solution(numbers, k):
    
    return numbers[(2 * (k - 1)) % len(numbers)]


# 뭔가 큐를 써야할 것 같음..  -> 생각보다 큐로 구현하면 복잡하고 시간 소요가 많이 됨
# 그래서 나머지 연산을 쓰는게 낫긴 할 듯