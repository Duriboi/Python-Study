def sub_to_hwa():
    c = (f - 32) * 5 / 9
    return c

def hwa_to_sub():
    f = c * 9 / 5 + 32
    return f

choice = int(input("1.화씨->섭씨 2.섭씨->화씨:"))
if choice == 1:
    f = float(input("화씨 온도:"))
    print(f"섭씨 온도: {sub_to_hwa():.2f}")

else:
    c = float(input("섭씨 온도:"))
    print(f"화씨 온도: {hwa_to_sub():.2f}")
