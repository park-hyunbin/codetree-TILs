n = input()

def even(n):
    sum = 0 
 
    if int(n) % 2 == 0 :
        for i in n : 
            i = int(i)
            sum += i
            if sum % 5 ==0 : 
                return True 
    else : 
        return False 

if even(n) : 
    print("Yes")
else : 
    print("No")
            
