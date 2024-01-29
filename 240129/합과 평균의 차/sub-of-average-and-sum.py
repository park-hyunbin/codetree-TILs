a,b,c = map(int,input().split())
arr = [a,b,c]

print(sum(arr))
print(sum(arr)//len(arr))
print(sum(arr)- sum(arr)//len(arr))