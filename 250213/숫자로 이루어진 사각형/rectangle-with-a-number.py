n = int(input())

def print_4(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print(cnt, end = ' ')
            cnt+=1
            if cnt > 9 : 
                cnt =1
        print()
print_4(n)