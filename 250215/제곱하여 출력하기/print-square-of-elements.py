n = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)) : 
    print(arr[i]*arr[i], end =' ')
