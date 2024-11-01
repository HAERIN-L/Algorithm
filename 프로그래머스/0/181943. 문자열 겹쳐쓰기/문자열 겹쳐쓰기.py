def solution(my_string, overwrite_string, s):
    
    prefix = my_string[:s]
    suffix = my_string[s+len(overwrite_string):]
    
    answer = prefix + overwrite_string + suffix
    return answer