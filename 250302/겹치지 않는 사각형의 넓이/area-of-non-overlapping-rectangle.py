OFFSET = 1000
MAX_R = 2000

# 입력받은 직사각형 리스트 
rects = [
    tuple(map(int, input().split()))
    for _ in range(3)
]

grid = [
    [0] * (MAX_R + 1) 
    for _ in range(MAX_R + 1)
]

for x1, y1, x2, y2 in rects:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET 

    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1 

last_x1, last_y1, last_x2, last_y2 = rects[-1] 
last_x1, last_y1 = last_x1 + OFFSET, last_y1 + OFFSET
last_x2, last_y2 = last_x2 + OFFSET, last_y2 + OFFSET

for x in range(last_x1, last_x2):
    for y in range(last_y1, last_y2):
        grid[x][y] = 0  # 마지막 직사각형 영역 삭제

area = sum(sum(row) for row in grid)

print(area)
