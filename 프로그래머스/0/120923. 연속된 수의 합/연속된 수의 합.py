def solution(num, total):
    middle = total / num
    # print(middle)
    start = int(middle - (num-1)/2)
    # print(start)
    return [i for i in range(start, start+num)]
