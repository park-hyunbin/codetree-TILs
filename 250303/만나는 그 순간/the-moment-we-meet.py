n, m = map(int, input().split())

# A의 이동 정보 저장
d_a = []
for _ in range(n):
    direction, distance = input().split()
    d_a.append((direction, int(distance)))

# B의 이동 정보 저장
d_b = []
for _ in range(m):
    direction, distance = input().split()
    d_b.append((direction, int(distance)))

# 초기 위치
pos_a = 0
pos_b = 0

# A와 B의 이동 기록 리스트
path_a = []
path_b = []

# A의 이동 기록
for direction, distance in d_a:
    for _ in range(distance):
        if direction == 'R':
            pos_a += 1
        else:
            pos_a -= 1
        path_a.append(pos_a)

# B의 이동 기록
for direction, distance in d_b:
    for _ in range(distance):
        if direction == 'R':
            pos_b += 1
        else:
            pos_b -= 1
        path_b.append(pos_b)

# 두 개의 객체가 만나는 순간 찾기
meet_time = -1
for i in range(min(len(path_a), len(path_b))):
    if path_a[i] == path_b[i]:
        meet_time = i + 1  # 1-based index로 출력
        break

print(meet_time)
