x,y = 0,0 
n = int(input())

for i in range(n) :
    dir, dist = input().split()
    dist = int(dist)

    if dir == 'N' : 
        y += dist 
    elif dir == 'E' : 
        x += dist
    elif dir == 'S' :
        y -= dist
    else : 
        x -= dist
print(x,y)