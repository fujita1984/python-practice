import os
import tkinter as tk
import openai

def function_name(event=None):
    
    # 環境変数からapikeyを取得
    openai.api_key = os.environ.get('YOUR_OPENAI_API_KEY')
    send_message = text_area_request.get("1.0", tk.END)

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens = 4000,
            messages=[
                {"role": "user", "content": send_message}
        ],
    )

    response_message = response.choices[0]["message"]["content"].strip()
    text_area_response.insert(tk.END, response_message + "\n")

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("your window name")

# 送信ボタンを作成
button = tk.Button(window, text="メッセージを送信", command=function_name)
button.pack(padx=20, pady=10)

# 送信用テキストエリアのラベルを作成
label = tk.Label(window, text="あなたのメッセージ")
label.pack(padx=20, pady=10)

# 送信用テキストエリアを作成
text_area_request = tk.Text(window)
text_area_request.pack(padx=20, pady=10)

# ラベルを作成
label = tk.Label(window, text="GPTのメッセージ")
label.pack(padx=20, pady=10)

text_area_response = tk.Text(window)
text_area_response.pack(padx=20, pady=10)

# Enterキーが押されたときに関数を実行するためのバインディングを追加
text_area_request.bind("<Return>", function_name)

# ウィンドウを表示
window.mainloop()