prices = {'아메리카노':2000, '카페라떼':2500, '카푸치노':3000}
sum = 0

while True:
    s= input('음료 종류 또는 종료:')
    if s == '종료':
        break
    elif s in prices:
        n= int(input(f'{s} 몇 잔? '))
        sum += prices[s] * n
    else:
        print('없는 음료입니다.')

print(f'총 금액은 {sum}원 입니다.')