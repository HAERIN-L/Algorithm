num = input().strip()

# 각 자리 숫자 합 계산
digit_sum = sum(int(digit) for digit in num)

# 숫자가 0이면서 각 자리 숫자의 합이 3의 배수인지 확인
if '0' in num and digit_sum % 3 == 0:
    # 가장 큰 수를 만들기 위해 각 자리 숫자를 내림차순으로 정렬하여 출력
    print(''.join(sorted(num, reverse=True)))
else:
    print(-1)
