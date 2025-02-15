n = int(input()) 

for i in range(n):
    for j in range(n):
        # 첫 번째 행, 마지막 행, 첫 번째 열, 마지막 열에 * 출력
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
