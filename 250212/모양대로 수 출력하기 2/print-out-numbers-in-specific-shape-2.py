n = int(input())
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt +=1
        print(cnt*2, end = ' ')
        if cnt > 3 : 
            cnt = 0
    print()