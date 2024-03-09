# 스택 자료구조 사용
import sys 

n = int(input())

for _ in range(n):
    stack =[]
    line = input()
    
    for t in line:
        if t =='(':
            stack.append(t)
        elif t ==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:  # for문의 else문
        if len(stack) ==0:
            print('YES')
        else:
            print('NO')

    