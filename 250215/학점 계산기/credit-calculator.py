n = int(input())
arr = list(map(float, input().split()))

sum = 0 
for i in arr : 
    sum += i 
print(round(sum/n,1))

avg = round(sum/n,1)

def score (avg) :
    if avg >=4.0 :
        print("Perfect")
    elif 4.0 > avg >=3.0 :
        print("Good")
    else : 
        print("Poor") 

score(avg)
