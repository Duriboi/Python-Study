import random

dice_a= random.randint(1,6)
dice_b= random.randint(1,6)

print(f'주사위1:{dice_a}, 주사위2:{dice_b}')

if dice_a>dice_b:
    print("주사위1이 이겼습니다.")
elif dice_a<dice_b:
    print("주사위2가 이겼습니다.")
else:
    print("비겼습니다.")
    