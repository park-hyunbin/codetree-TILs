list = []
satisfied = False 
for i in range(5):
    a = int(input())
    list.append(a)

for i in list : 
    if i %3 != 0 :
        satisfied =True 
        break

if satisfied ==True : 
    print(0)
else : 
    print(1)