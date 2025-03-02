n = int(input())

# 입력된 선분 정보를 리스트로 저장
segments = [list(map(int, input().split())) for _ in range(n)]

# 선분의 최대 끝점 찾기 (배열 크기 설정)
max_position = max(b for _, b in segments)
blocks = [0] * (max_position + 1)

# 각 구간에 대해 겹치는 부분을 표시
for a, b in segments:
    for i in range(a, b):  # b를 포함하지 않는 구간
        blocks[i] += 1

# 최대 겹치는 선분 개수 찾기
max_num = max(blocks)
print(max_num)
