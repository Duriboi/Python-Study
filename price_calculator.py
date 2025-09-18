age=int(input("나이를 입력하세요: "))

if age<8:
    price=5000*0.7
elif age>=8 and age<60:
    price=5000;
else:
    price=5000*0.8

print(f'입장료는 {price}원 입니다.')