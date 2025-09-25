import random

answer = random.randint(1, 100)

while True:
    guess = int(input("1부터 100 사이의 숫자를 맞혀보세요: "))
    if guess < answer:
        print("더 큰 수를 입력하세요.")
    elif guess > answer:
        print("더 작은 수를 입력하세요.")
    else:
        print("정답입니다!")
        break
    