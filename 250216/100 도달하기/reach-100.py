n = int(input())

arr = [1, n]

for i in range(1,100) : 
    a = arr[i] + arr[i-1]
    arr.append(a)
    if a >= 100 : 
        break 

for i in arr : 
    print(i, end = ' ')