def solution(score):
    average = [sum(i)/2 for i in score]
    
    sort_list = sorted(average, reverse=True)
    return [sort_list.index(i) +1 for i in average]
