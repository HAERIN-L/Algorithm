import sys

n = int(sys.stdin.readline()) #input 쓰면 시간 초과될 거 같앗음..

stack =[]

for _ in range(n):
    com = sys.stdin.readline().split() #공백을 기준으로 분리 split
    
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'pop':
        if len(stack) == 0: #비어있는지 확인
            print(-1)
        else:
            print(stack.pop())
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] =='top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            
     





