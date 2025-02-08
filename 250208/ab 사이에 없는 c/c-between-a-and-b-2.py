a,b,c = map(int,input().split())

satisfied = False

for i in range(1,a):
    if a<= c*i <=b :
        satisfied = True 
        break
    else : 
        satisfied = False

if satisfied == True : 
    print("NO")
else : 
    print("YES") 