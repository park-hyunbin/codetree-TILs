s = input()
length = len(s)

exists = False
exists1 = False

for i in range(length - 1):
    if s[i:i + 2] == 'ee':
        exists = True 
        break
    else : 
        exists = False
        

for i in range(length - 1):
    if s[i:i + 2] == 'ab':
        exists1 = True
        break
    else : 
        exists1 = False

if exists == True and exists1 == True : 
    print("Yes Yes")
elif exists == True and exists1 == False :
    print("Yes No")
elif exists == False and exists1 == True : 
    print("No Yes")
else : 
    print("No No")