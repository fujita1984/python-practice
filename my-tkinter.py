import os
import tkinter as tk
import openai

def ini_history(event=None):
    message_all = [{"role":"system","content":"性格：子供,振る舞い：語尾に「だよ」をつける"}]
    text_area_request.delete("1.0", tk.END)
    text_area_response.delete("1.0", tk.END)
    print(message_all)

def send_request(event=None):
    
    if not event or (event.keysym == "Return" and not event.state & 0x1):

        openai.api_key = os.environ.get('YOUR_OPENAI_API_KEY')
        send_message = text_area_request.get("1.0", tk.END)
        message_all.append({"role":"user","content":send_message})

        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                max_tokens = 500,
                messages = message_all
        )

        response_message = response.choices[0]["message"]["content"].strip()
        message_all.append({"role":"assistant","content":response_message})
        print(message_all)
        text_area_response.insert(tk.END, response_message + "\n")

message_all = [{"role":"system","content":"性格：子供,振る舞い：語尾に「だよ」をつける"}]

window = tk.Tk()
window.title("your window name")

top_frame = tk.Frame(window)
top_frame.pack()

button_send = tk.Button(top_frame, text="メッセージを送信", command=send_request)
button_reset = tk.Button(top_frame, text="履歴を消す", command=ini_history)
button_send.pack(padx=20, pady=10, side=tk.LEFT)
button_reset.pack(padx=20, pady=10, side=tk.LEFT)

label_request = tk.Label(window, text="あなたのメッセージ")
label_request.pack(padx=20, pady=10)

text_area_request = tk.Text(window)
text_area_request.pack(padx=20, pady=10)

label_response = tk.Label(window, text="GPTのメッセージ")
label_response.pack(padx=20, pady=10)

text_area_response = tk.Text(window)
text_area_response.pack(padx=20, pady=10)

text_area_request.bind("<Return>", send_request)

window.mainloop()