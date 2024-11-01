import re

def solution(new_id):
    # 1단계. 대문자 -> 소문자
    new_id = new_id.lower()
    
    #2단계. 필요 문자 빼고 제거 -> re.sub() 사용
    new_id = re.sub(r'[^a-z0-9-_.]','',new_id)
    
    #3단계. '.' 연속인거 치환 -> re.sub()
    new_id = re.sub(r'\.+', '.', new_id)
    
    #4단계. 마침표가 처음이나 끝이면 제거 
    new_id = new_id.strip('.')
    
    #5단계. new id가 빈 문자열이면 a 대입
    if not new_id:
        new_id ='a'
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    #7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id