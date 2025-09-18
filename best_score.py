score1=int(input('1차 시험 점수:'))
score2=int(input('2차 시험 점수:'))
score3=int(input('3차 시험 점수:'))

max=0

if score1>max:
    max=score1

if score2>max:
    max=score2

if score3>max:
    max=score3

print(f'최고 점수는 {max}점 입니다.')
