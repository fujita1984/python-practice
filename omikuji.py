import tkinter as tk
import random

def omikuji():
    results = ["大吉", "吉", "凶"]
    result = random.choice(results)
    result_label.config(text=result)

# ウィンドウを作成
window = tk.Tk()
window.title("おみくじアプリ")

# ラベルを作成
result_label = tk.Label(window, text="", font=("Arial", 24), padx=20, pady=10)
result_label.pack()

# おみくじボタンを作成
omikuji_button = tk.Button(window, text="おみくじを引く", command=omikuji, font=("Arial", 16))
omikuji_button.pack()

# ウィンドウを表示
window.mainloop()
