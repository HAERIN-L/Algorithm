def solution(array, commands):
    
    answer=[]
    
    for i in range(len(commands)):
        cut = array[commands[i][0]-1:commands[i][1]]
        cut.sort()
        answer.append(cut[commands[i][2]-1])
    
    return answer

# 1. array 입력 받기
# 2. commands 입력 받기 근데 1번이 i, 2번이 j, 배열에서 받을 수 몇번째인지 k
# 3. answer에 k번째가 return한 값 받기
# 결론적으로 이 문제는 배열에서 두번째 배열의 첫번째인자, 두번째 인자인 숫자로 자르고 그 뒤에 숫자 있는걸 뽑아서 다른 배열에 append를 해줘서 그걸 뽑아줘야하는거임.

# 그럼 일단 commands의 배열 수만큼 돌아돌아