import random

a= random.randint(1,10)
answer = int(input("선택한 수를 맞춰보세요(1~10):"))
print(a==answer, "정답은", a)