n = int(input())

for i in range(n):
  s = list(input().split()) # 공백 기준으로 단어 분리 후, 리스트로 저장

  for j in s:
    print(j[::-1], end=' ') # 단어 뒤집어서 출력하기
