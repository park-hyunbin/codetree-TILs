arr = ["banana", "apple", "grape","blueberry","orange"]
str = input()

satisfied = []

for i in arr : 
    if i[2] == str or i[3] == str : 
        satisfied.append(i)

for i in satisfied : 
    print(i)
print(len(satisfied))

