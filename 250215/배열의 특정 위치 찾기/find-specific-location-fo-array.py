arr = list(map(int, input().split()))

filtered_arr = arr[1::2]  
filtered_arr_1 = arr[2:9:3] 

sum_val = sum(filtered_arr) 
avg2 = sum(filtered_arr_1) / len(filtered_arr_1) 
avg = round(avg2, 1)

print(sum_val, avg)
