#n번째 원소를 temp에 저장
#temp = a[n-1]
#나머지 원소를 오른쪽으로 shift
#for row in range(n-1):
#   a[row][col] = temp

n,t = tuple(map(int,input().split()))
u = list(map(int,input().split()))
d = list(map(int,input().split()))

for _ in range(t):
    temp = u[n-1]
    
    for i in range(n-1,0,-1):
        u[i] = u[i-1]
    u[0] = d[n-1]
    
    for i in range(n-1,0,-1):
        d[i] = d[i-1]
    d[0] = temp

for elem in u : 
    print(elem, end = ' ')
print()

for elem in d : 
    print(elem, end = ' ')