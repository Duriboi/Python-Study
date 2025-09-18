a=7
b=11
temp = a
a=b
b=temp
print(a,b) #C언어 등에서는 temp 변수를 사용해서 교환

c=7
d=11
c,d=d,c
print(c,d) #파이썬에서는 튜플을 이용해서 교환(결과는 같다.)