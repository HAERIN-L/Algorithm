def solution(hp):
    count = 0
    for power in [5,3,1]:
        count += hp//power
        hp %=power
    return count