delivery_fee=2000
level = input('회원등급(우수 or 일반):')

price= int(input('주문금액:'))

if level=='우수':
    print('결제금액:', price)
elif price>=20000:
    print('결제금액:', price)
else:
    print('결제금액:', price+delivery_fee)
