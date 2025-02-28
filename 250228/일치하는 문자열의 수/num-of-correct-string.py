n,a = input().split()

n = int(n)

cnt = 0 

for _ in range(n) : 
    str = input()
    if str == a : 
        cnt +=1
print(cnt)