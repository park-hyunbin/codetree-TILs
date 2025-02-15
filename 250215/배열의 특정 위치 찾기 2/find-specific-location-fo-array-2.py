arr = list(map(int,input().split()))

sum = 0 
sum_val = 0 

for i in range(len(arr)) : 
    if i%2==0 : 
        sum+=arr[i]
    else : 
        sum_val+= arr[i]

if sum >= sum_val :
    print(sum-sum_val)
else : 
    print(sum_val - sum)