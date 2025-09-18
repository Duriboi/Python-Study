import math

def square():
    width = int(input("사각형의 가로 길이: "))
    height = int(input("사각형의 세로 길이: "))
    return width * height

def triangle():
    width = int(input("삼각형의 밑변 길이: "))
    height = int(input("삼각형의 높이: "))
    return width * height / 2

def circle():
    radius = int(input("원의 반지름 길이: "))
    return math.pi * radius * radius

first_shape_type = int(input("1.사각형 2.삼각형 3.원: "))
second_shape_type = int(input("1.사각형 2.삼각형 3.원: "))

if first_shape_type == 1:
    area1 = square()
elif first_shape_type == 2:
    area1 = triangle()
else:
    area1 = circle()

if second_shape_type == 1:
    area2 = square()
elif second_shape_type == 2:
    area2 = triangle()
else:
    area2 = circle()

if area1 > area2:
    print("첫 번째 도형이 더 넓습니다.")
elif area1 < area2:
    print("두 번째 도형이 더 넓습니다.")
else:
    print("두 도형의 넓이가 같습니다.")
    
