n = int(input()) 
given_str = input().split()  # 공백 기준으로 문자열 리스트 생성

arr = [] 
temp = []  

for elem in given_str:
    for char in elem: 
        temp.append(char)
        if len(temp) == 5:  
            arr.append(temp)
            temp = []

if temp:
    arr.append(temp)

for row in arr:
    print("".join(row))
