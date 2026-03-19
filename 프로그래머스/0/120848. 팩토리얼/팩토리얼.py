import math

def solution(n):
    for i in range(1,12):
        if math.factorial(i) > n:
            return i-1