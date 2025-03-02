OFFSET = 1000
MAX_R = 2000 

rects1 = [
    tuple(map(int,input().split()))
]

rects2 = [
    tuple(map(int,input().split()))
]

grid = [
    [0] * (MAX_R+1)
    for _ in range(MAX_R+1)
]

for x1,x2,y1,y2 in rects1 : 
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,y1):
        for y in range(x2,y2):
            grid[x][y] = 1

area = sum(sum(row) for row in grid)
print(area)