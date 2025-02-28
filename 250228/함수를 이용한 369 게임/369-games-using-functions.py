a, b = map(int, input().split())

def all_different(n):
    n = str(n) 
    for digit in n:
        if digit in "369": 
            return True
    return False 

def three_number(n):
    return n % 3 == 0  

cnt = 0

for i in range(a, b+1):
    if all_different(i) or three_number(i):  
        cnt += 1

print(cnt)
