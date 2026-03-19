def solution(emergency):
    
    sort_list = sorted(emergency, reverse=True)
    return [sort_list.index(i)+1 for i in emergency]
