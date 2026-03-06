def solution(s):
    result =[]
    
    for i in set(s):
        if s.count(i) == 1:
            result.append(i)
    return ''.join(sorted(result))
            
