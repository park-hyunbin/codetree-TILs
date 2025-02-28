string = input().split()

found = False  

for index, char in enumerate(string[0]):
    if char == string[1]:
        print(index)
        found = True
        break

if not found:
    print('No')
