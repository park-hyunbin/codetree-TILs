a,b = map(int,input().split())

sum = a+b

s = str(sum)

cnt = 0 

for i in s : 
    if i == '1' : 
        cnt+=1 
print(cnt)
