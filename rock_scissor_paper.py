import random

a= random.randint(1,3)

user= input("가위, 바위, 보 중 하나를 선택하세요:")

if a==1:
    computer='가위'
elif a==2:
    computer='바위'
else:
    computer='보'
print(f"컴퓨터는 {computer}를 선택했습니다.")

if user==computer:
    print("비겼습니다.")

elif (user=='가위' and computer=='보') or (user=='바위' and computer=='가위') or (user=='보' and computer=='바위'):
    print("사용자가 이겼습니다.")

else:
    print("컴퓨터가 이겼습니다.")