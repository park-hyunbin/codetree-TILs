num = input()
new_num = num.split('-')
new_num[0], new_num[1], new_num[2] = new_num[0], new_num[2], new_num[1]
result = '-'.join(new_num)
print(result)