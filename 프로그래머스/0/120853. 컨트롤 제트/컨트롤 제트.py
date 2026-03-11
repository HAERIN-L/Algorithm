def solution(s):
    stack = []
    for char in s.split():
        if char == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(char))
            
    return sum(stack)
