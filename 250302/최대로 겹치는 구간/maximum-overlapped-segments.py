n = int(input())

events = []  # (좌표, 변화량) 리스트

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))  # 선분이 시작하는 지점 +1
    events.append((b, -1))  # 선분이 끝나는 지점 -1

# 좌표 정렬 (같은 위치일 경우, 종료(-1)가 시작(+1)보다 먼저 처리되도록)
events.sort()

# 스위핑 진행
current_overlap = 0
max_overlap = 0

for _, change in events:
    current_overlap += change  # 현재 겹치는 선분 개수 변경
    max_overlap = max(max_overlap, current_overlap)  # 최대 겹치는 개수 갱신

print(max_overlap)
