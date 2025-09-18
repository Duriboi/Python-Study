import random
a= random.randint(1,100)
b=random.randint(1,100)
if a<b:
    a,b=b,a
print(a,b)