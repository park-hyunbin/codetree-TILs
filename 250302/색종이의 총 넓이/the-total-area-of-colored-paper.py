OFFSET = 100 
MAX_R = 200 
square_size = 8

n = int(input())

rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

grid = [
    [0] * (MAX_R +1)
    for _ in range(MAX_R+1)
]

for x, y in rects : 
    x1, y1 = x+ OFFSET, y + OFFSET

    for i in range(x1, x1+square_size): 
        for j in range(y1, y1+square_size):
            grid[i][j] = 1  

area = sum(sum(row) for row in grid)
print(area)