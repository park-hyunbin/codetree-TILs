n = int(input())

arr = []
cnt = 0 
cntt = 0 

while True : 
    cntt += 1
    arr.append(cntt*n)
    if cntt*n % 5 == 0 : 
        cnt +=1 
        if cnt ==2 : 
            break

for i in arr : 
    print(i, end = ' ')