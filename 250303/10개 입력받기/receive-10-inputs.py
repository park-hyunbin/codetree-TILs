arr = list(map(int, input().split()))

avg = 0 
sum_arr = 0 
cnt = 0 

for elem in arr:
	if elem == 0:
		break
	cnt += 1
	sum_arr += elem 
	avg = sum_arr / cnt


print(sum_arr, round(avg,1))
