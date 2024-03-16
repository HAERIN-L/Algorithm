def compress_coordinates(coords):
    # 정렬된 좌표와 원래 좌표의 매핑을 저장할 딕셔너리
    rank = {v: i for i, v in enumerate(sorted(set(coords)))}
    # 압축된 좌표를 저장할 리스트
    compressed = [rank[x] for x in coords]
    return compressed

n = int(input())
coords = list(map(int, input().split()))

# 좌표 압축 실행
compressed_coords = compress_coordinates(coords)

# 결과 출력
print(' '.join(map(str, compressed_coords)))

