import tkinter as tk
import random

# 카드 덱 구성 (A, 2~10, J, Q, K)
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# 카드 점수 매기기
def get_card_value(card):
    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K', '10']:
        return 0
    else:
        return int(card)

# 점수 계산 (10을 넘으면 나머지 사용)
def calculate_score(hand):
    total = sum(get_card_value(card) for card in hand)
    return total % 10

# 게임 실행
def play_game():
    # 카드 섞기
    player_hand = random.sample(cards, 2)
    banker_hand = random.sample(cards, 2)

    # 점수 계산
    player_score = calculate_score(player_hand)
    banker_score = calculate_score(banker_hand)

    # 결과 판정
    if player_score > banker_score:
        result = "플레이어 승리!"
    elif player_score < banker_score:
        result = "뱅커 승리!"
    else:
        result = "무승부!"

    # GUI 업데이트
    player_label.config(text=f"플레이어 카드: {player_hand} (점수: {player_score})")
    banker_label.config(text=f"뱅커 카드: {banker_hand} (점수: {banker_score})")
    result_label.config(text=f"결과: {result}")

# GUI 구성
window = tk.Tk()
window.title("바카라 게임")
window.geometry("400x250")

title_label = tk.Label(window, text="🎲 바카라 게임", font=("Helvetica", 16))
title_label.pack(pady=10)

player_label = tk.Label(window, text="플레이어 카드: ")
player_label.pack()

banker_label = tk.Label(window, text="뱅커 카드: ")
banker_label.pack()

result_label = tk.Label(window, text="결과:")
result_label.pack(pady=10)

play_button = tk.Button(window, text="게임 시작", command=play_game)
play_button.pack(pady=10)

# 실행
window.mainloop()
