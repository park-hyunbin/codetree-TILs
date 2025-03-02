n = int(input())

numbers = [
    int(input()) 
    for _ in range(n)]  

max_count = 1 
current_count = 1  

for i in range(1, n):
    if numbers[i] == numbers[i - 1]: 
        current_count += 1
    else:
        max_count = max(max_count, current_count)  # 최대 연속 개수 갱신
        current_count = 1  # 새로운 숫자로 초기화

max_count = max(max_count, current_count)

print(max_count)
