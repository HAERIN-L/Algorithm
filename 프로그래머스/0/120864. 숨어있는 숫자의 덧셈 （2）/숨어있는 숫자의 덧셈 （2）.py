import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    return sum(int(n) for n in numbers)
