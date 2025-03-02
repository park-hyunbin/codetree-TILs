n = int(input())

MAX_SIZE = 101
grid = [
    [0] * MAX_SIZE 
    for _ in range(MAX_SIZE)
]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    # 주어진 사각형 범위 내의 좌표를 1로 채움
    for i in range(x1, x2):  
        for j in range(y1, y2):  
            grid[i][j] = 1  # 직사각형 부분 표시

area = sum(sum(row) for row in grid)

print(area)
