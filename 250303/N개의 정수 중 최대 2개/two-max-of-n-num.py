n = int(input())
arr = list(map(int, input().split()))  # 입력을 정수 리스트로 변환

arr_srt = sorted(arr, reverse =True)
print(arr_srt[0],arr_srt[1])