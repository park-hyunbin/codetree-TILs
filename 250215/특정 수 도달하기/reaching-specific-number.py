arr = list(map(int, input().split()))

sum = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] >= 250:  
        break
    sum += arr[i]
    cnt += 1

print(sum, format(sum / cnt, ".1f")) 
