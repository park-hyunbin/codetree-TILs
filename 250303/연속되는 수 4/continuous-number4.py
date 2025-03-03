n = int(input())
numbers = [int(input()) for _ in range(n)]

max_count = 1
current_count = 1

for i in range(1, n):
    if (numbers[i] > numbers[i - 1]) :
        current_count += 1
    else:
        current_count = 1  # 부호가 바뀔 때 
        
    max_count = max(max_count, current_count) 

print(max_count)
