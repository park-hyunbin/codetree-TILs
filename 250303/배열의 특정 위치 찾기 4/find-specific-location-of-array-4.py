arr = list(map(int, input().split()))
cnt = 0
sum_elem = 0 

for elem in arr:
	if elem == 0 : 
		break
	elif elem %2 == 0:
		cnt += 1
		sum_elem+=elem

print(cnt, sum_elem)
