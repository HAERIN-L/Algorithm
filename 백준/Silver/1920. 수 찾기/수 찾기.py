from bisect import bisect_left

def binary_search(arr, target):
    index = bisect_left(arr, target)
    return index < len(arr) and arr[index] == target

n = int(input())
array = list(map(int, input().split()))
array.sort()  # 이진 탐색을 위한 정렬

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(1 if binary_search(array, target) else 0)
