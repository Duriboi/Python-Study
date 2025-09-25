import random

print('1~100 중 숫자 하나를 정하세요.')
num= int(input('숫자 입력: '))
low=1
high=100
times=0

while True:
    times+=1    
    guess=random.randint(low,high)
    print(f'컴퓨터의 추측: {guess}')
    if num==guess:
        print(f'정답입니다! {times}번 만에 맞췄습니다.')
        break
    elif num>guess:
        print('더 큰 수를 입력하세요.')
        low=guess+1
    else:
        print('더 작은 수를 입력하세요.')
        high=guess-1
