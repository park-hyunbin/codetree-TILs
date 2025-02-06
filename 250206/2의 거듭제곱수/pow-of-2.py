n = int(input())
x = 0
while 2<=n<=1024:
    if n%2 == 0 : 
        x+=1
        n//= 2
    else : 
        break      
print(x)