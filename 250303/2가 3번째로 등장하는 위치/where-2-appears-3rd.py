n = int(input())
arr = list(map(int, input().split()))  # 입력을 정수 리스트로 변환

idx = 0  # 2가 등장한 횟수
position = -1  # 기본값: 2가 세 번째 등장하지 않으면 -1 유지

for i in range(n): 
    if arr[i] == 2: 
        idx += 1
        if idx == 3:  # 세 번째 2를 찾았을 때
            position = i+1
            break  # 반복문 종료
            
print(position)
