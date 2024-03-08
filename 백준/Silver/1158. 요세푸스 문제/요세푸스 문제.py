import sys

n, k = map(int, input().split())
result=[]
dq = ([i for i in range(1, n+1)])
c =0

while dq:
    c = (c + k-1) % len(dq)
    result.append(str(dq.pop(c)))

print("<",', '.join(result),">", sep="") 