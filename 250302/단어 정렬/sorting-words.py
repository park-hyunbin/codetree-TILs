n = int(input())

words = []  

for _ in range(n):
    words.append(input())  

sorted_words = sorted(words)  
result = '\n'.join(sorted_words)  

print(result)
