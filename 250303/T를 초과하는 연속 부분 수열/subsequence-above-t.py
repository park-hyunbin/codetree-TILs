n,t = map(int,input().split())
numbers = input().split()

max_count = 1
current_count = 1

for num in numbers :
    for i in range(1, n): 
        if int(num) > t : 
            if (numbers[i] > numbers[i - 1]) :
                current_count += 1
            else:
                current_count = 1  
                
    max_count = max(max_count, current_count) 

print(max_count)
