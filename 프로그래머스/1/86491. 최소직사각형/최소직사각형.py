def solution(sizes):
    w =[]
    h =[]
    
    for x,y in sizes:
        big = max(x,y)
        small = min(x,y)
        
        w.append(big)
        h.append(small)
        
    return max(w)*max(h)
