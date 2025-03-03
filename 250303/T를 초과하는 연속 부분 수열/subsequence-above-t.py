n, t = map(int, input().split())
numbers = list(map(int, input().split())) 

max_count = 1
current_count = 0

for i in range(1, n): 
    if numbers[i] and numbers[i-1] > t:  
        current_count += 1
    else:
        current_count = 0

    max_count = max(max_count, current_count)  # 최대 길이 갱신

print(max_count)
