import random
a= random.randint(1,10)
b=random.randint(1,10)
my_quotient = int(input(f"{a}를 {b}로 나눈 몫은?"))
print(a//b==my_quotient, "정답은", a//b)
