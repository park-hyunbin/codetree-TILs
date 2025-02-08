n = int(input())

satisfied = False 

for i in range(2,n):
    if n%i ==0 : 
        break 
        satisfied = False 
    else : 
        satisfied = True

if satisfied == False : 
    print("C")
else : 
    print("P")
    