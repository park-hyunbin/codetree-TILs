n = int(input())
arr = list(map(int,input().split()))

sum = []

for i in arr : 
    if i%2== 0 : 
        sum.append(i)

for i in sum : 
    print(i, end = ' ')