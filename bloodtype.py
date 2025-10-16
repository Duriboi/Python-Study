blood = {'A':0, 'B':0, 'O':0, 'AB':0}

while True:
    s = input('혈액형(A, B, O, AB) 또는 종료:')
    if s == '종료':
        break
    elif s in blood:
        blood[s] += 1
    else:
        print('잘못된 혈액형입니다.')

for k, v in blood.items():
    print(k, v)

