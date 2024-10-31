def solution(myString, pat):
    
    change = myString.translate(str.maketrans('AB','BA'))
    
    return 1 if pat in change else 0