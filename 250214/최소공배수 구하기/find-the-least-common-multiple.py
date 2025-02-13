n,m = map(int,input().split())

def num(n,m):
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0 :
            gcd = i
            a = gcd * (m//gcd)* (n//gcd)
            return a 

print(num(n,m))