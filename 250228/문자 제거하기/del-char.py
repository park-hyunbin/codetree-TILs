string = input()

leng = len(string)

arr = list(string)

# 문자가 하나 남을 때까지 반복합니다.
while leng > 1:
	# 정수를 입력받습니다.
	a = int(input())
		
	# 정수가 문자열의 길이 이상이면 마지막 문자를 가리키게 변경합니다.
	if a >= leng:
		a = leng - 1
		
	# a번 자리의 원소를 제거합니다.
	arr.pop(a)
	leng -= 1
	
	# list를 문자열로 변환합니다.
	string = ''.join(arr)
	
	# 현재 문자열을 출력합니다.
	print(string)
