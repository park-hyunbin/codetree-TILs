# Offset과 최대 크기 설정
OFFSET = 1000
MAX_R = 2000

# 첫 번째 직사각형 입력
x1, y1, x2, y2 = map(int, input().split())
# 두 번째 직사각형 입력
x3, y3, x4, y4 = map(int, input().split())

# 좌표를 Offset 적용하여 음수 방지
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
x3, y3, x4, y4 = x3 + OFFSET, y3 + OFFSET, x4 + OFFSET, y4 + OFFSET

# 첫 번째 직사각형의 가로, 세로 길이
width1 = x2 - x1
height1 = y2 - y1

# 겹치는 영역 계산
overlap_x1 = max(x1, x3)
overlap_y1 = max(y1, y3)
overlap_x2 = min(x2, x4)
overlap_y2 = min(y2, y4)

# 겹치는 부분이 존재하는지 확인
if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
    overlap_width = overlap_x2 - overlap_x1
    overlap_height = overlap_y2 - overlap_y1
else:
    overlap_width = 0
    overlap_height = 0

# 첫 번째 직사각형이 완전히 덮이지 않았을 경우 필요한 최소 직사각형 찾기
remaining_width = max(width1 - overlap_width, width1)  # 남은 가로 길이
remaining_height = max(height1 - overlap_height, height1)  # 남은 세로 길이

# 추가 직사각형의 최소 크기
min_rectangle_area = remaining_width * remaining_height

# 출력: 첫 번째 직사각형을 덮기 위한 최소 추가 직사각형 넓이
print(min_rectangle_area)
