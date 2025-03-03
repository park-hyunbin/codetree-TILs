n = int(input())

numbers = [
    int(input()) 
    for _ in range(n)]  

max_count = 1 
current_count = 0
current_count_1 = 0

for i in range(1, n):
    if numbers[i] and numbers[i - 1] > 0 : 
        current_count += 1
    elif numbers[i] and numbers[i-1] < 0 : 
        current_count_1 += 1 
    else:
        max_count = max(max_count, current_count, current_count_1)  
        current_count = 1 

max_count = max(max_count, current_count, current_count_1)

print(max_count)
