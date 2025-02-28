string = input().split()  # 공백 기준으로 문자열 리스트 생성

if not string:  # 입력이 비어있을 경우 처리
    print(-1)
else:
    concat_str = ' '.join(string)  # 리스트를 하나의 문자열로 변환
    last_char = string[-1][0]  # 마지막 단어의 첫 번째 문자

    found = False  # 문자를 찾았는지 여부 확인
    for index, char in enumerate(string[0]):
        if char == last_char:
            print(index)
            found = True
            break

    if not found:
        print('No')  # 문자가 없을 경우 -1 출력
