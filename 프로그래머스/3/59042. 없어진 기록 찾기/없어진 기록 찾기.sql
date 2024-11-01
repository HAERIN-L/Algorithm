SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS # 동물 보호소에서 입양 보낸 동물의 정보를 담음
LEFT JOIN ANIMAL_INS USING (ANIMAL_ID)
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID




# 입양 간 기록은 있지만, 보호소에 들어온 기록은 없는 동물 ID랑 이름을 ID 순으로 조회 (B에는 있지만 A에는 없는 것)
# ANIMAL_INS는 동물 보호소에 들ㅇㅓ온 정보 : A
# ANIMAL_OUTS 동물 보호소에서 입양 보낸 동물의 정보 : B