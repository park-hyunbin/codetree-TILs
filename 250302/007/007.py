arr = input().split()

class Secret:
    def __init__(self, co, me, ti):
        self.k = co
        self.e = me
        self.m = ti

student1 = Secret(arr[0], arr[1], arr[2])
print("secret code :",student1.k) 
print("meeting point :",student1.e) 
print("time :",student1.m) 
