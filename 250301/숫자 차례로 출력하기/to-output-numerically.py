n = int(input())

def print_n(n):    # 1부터 n번째 줄까지 별을 출력하는 함수
    if n == 0:        # 종료 조건
        return
    
    for i in range(n):
        print(i+1,end=' ')   
    print()
    for i in range(n,0,-1):
        print(i,end=' ') 
print_n(n)