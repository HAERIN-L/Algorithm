from bisect import bisect_left, bisect_right


#이진 탐색 위한 lowerBount와 upperBound 함수 정의
def lower_bound(arr, target):
    return bisect_left(arr, target)

def upper_bound(arr, target):
    return bisect_right(arr, target)

n= int(input())
cards = list(map(int, input().split()))
cards.sort() # 이진 탐색하기 위해서 정렬

m = int(input())
targets = list(map(int, input().split()))

result={} # 결과 저장 딕셔너리

# 각 타겟에 대한 개수 찾기
for target in targets:
    if target not in result:
        result[target] = upper_bound(cards, target) - lower_bound(cards, target)

print(' '.join(str(result[x]) for x in targets))