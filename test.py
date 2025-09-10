import tkinter as tk
import random

# 랜덤 숫자 선택
secret_number = random.randint(1, 100)

# 버튼 클릭 시 실행되는 함수
def check_guess():
    try:
        guess = int(entry.get())
        if guess < secret_number:
            result_label.config(text="너무 작습니다.")
        elif guess > secret_number:
            result_label.config(text="너무 큽니다.")
        else:
            result_label.config(text="정답입니다!")
    except ValueError:
        result_label.config(text="숫자를 입력하세요.")

# GUI 생성
window = tk.Tk()
window.title("숫자 맞추기 게임")
window.geometry("300x200")

# 위젯 추가
label = tk.Label(window, text="1부터 100 사이 숫자를 맞춰보세요!")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="확인", command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# GUI 실행
window.mainloop()
