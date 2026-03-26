from collections import Counter

def solution(array):
    count = Counter(array)
    max_count = max(count.values())
    
    modes = [k for k,v in count.items() if v == max_count]
    
    return modes[0] if len(modes) == 1 else -1
    
    # return max(array, key=array.count) 중복값 처리가 안대서 후퇴~
    
