n = int(input())

numbers = [int(input()) for _ in range(n)]

if n == 1:
    print(1)
    exit()

max_count = 1
current_count = 1

for i in range(1, n):
    if (numbers[i] > 0 and numbers[i - 1] > 0) or (numbers[i] < 0 and numbers[i - 1] < 0):
        current_count += 1  # 같은 부호일 때 증가
    else:
        max_count = max(max_count, current_count)  # 최댓값 갱신
        current_count = 1  # 새로운 연속 구간 시작

max_count = max(max_count, current_count)  # 마지막 연속 구간 반영

print(max_count)
