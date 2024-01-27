time = input().split(":")

# 시간과 분을 정수로 변환
hour = int(time[0])
minute = int(time[1])

# 1시간 더하기
hour += 1

# 출력
print(f"{hour}:{minute:02d}")