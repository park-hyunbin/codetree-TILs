n = int(input())

def add(n):
    sum = 0 
    for i in range(n+1):
        sum += i
        ans = sum //10
    return ans


print(add(n))