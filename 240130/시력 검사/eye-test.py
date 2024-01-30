left = float(input())
right = float(input())

if left and right >= 1.0 : 
    print('High')
elif left and right >= 0.5 and left and right <1.0 : 
    print('Middle')
else : 
    print('Low')