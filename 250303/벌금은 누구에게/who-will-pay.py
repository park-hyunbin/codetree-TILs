n, m, k = map(int, input().split())

arr = []

for i in range(m):
    num = int(input())
    arr.append(num)

    if arr.count(num) == k : 
        print(num)
        break
else : 
    print(-1)

