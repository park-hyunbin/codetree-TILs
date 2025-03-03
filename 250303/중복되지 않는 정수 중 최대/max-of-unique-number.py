n = int(input())
arr = list(map(int, input().split()))

def find_max_unique(arr):
    # 각 숫자의 등장 횟수를 저장하는 딕셔너리 생성
    count_dict = {}
    
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1  # 등장 횟수 증가
    
    # 등장 횟수가 1인 숫자만 필터링
    unique_numbers = [num for num in arr if count_dict[num] == 1]

    # 중복되지 않는 숫자가 없으면 -1 반환, 있으면 최댓값 반환
    return max(unique_numbers) if unique_numbers else -1

print(find_max_unique(arr))