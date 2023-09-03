import os
import tkinter as tk
import json
import mysql.connector
import openai

def connect_mysql():
    # MySQLサーバーへの接続情報
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'test',
        'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)
    return cnx

def new_chat(event=None):
    
    global message_all
    global current_id

    message_all = [{"role":"system","content":"性格：子供,振る舞い：語尾に「だよ」をつける"}]
    text_area_request.delete("1.0", tk.END)
    text_area_response.delete("1.0", tk.END)

    try:
        cnx = connect_mysql()
        print('MySQLサーバーへの接続に成功しました。')

        cursor = cnx.cursor(dictionary=True)
        query = "INSERT INTO `test`(`json`) VALUES ('null')"
        cursor.execute(query)
        current_id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print('MySQLサーバーへの接続に失敗しました。エラー: {}'.format(err))

def send_request(event=None):

    global message_all
    
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
        text_area_response.insert(tk.END, response_message + "\n")
        register()

def register():

    global message_all
    global current_id

    my_json = json.dumps(message_all)

    # MySQLサーバーへの接続
    try:
        cnx = connect_mysql()
        print('MySQLサーバーへの接続に成功しました。')
        cursor = cnx.cursor()
        query = 'UPDATE `test` SET `json`= %s WHERE `id`=%s;'
        cursor.execute(query,(my_json,current_id,))
        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print('MySQLサーバーへの接続に失敗しました。エラー: {}'.format(err))

message_all =[]
current_id = ''

window = tk.Tk()
window.title("your window name")

top_frame = tk.Frame(window)
top_frame.pack()

button_send = tk.Button(top_frame, text="send", command=send_request)
button_reset = tk.Button(top_frame, text="clear", command=new_chat)
button_send.pack(padx=20, pady=10, side=tk.LEFT)
button_reset.pack(padx=20, pady=10, side=tk.LEFT)

label_request = tk.Label(window, text="your message")
label_request.pack(padx=20, pady=10)

text_area_request = tk.Text(window)
text_area_request.pack(padx=20, pady=10)

label_response = tk.Label(window, text="gpt's message")
label_response.pack(padx=20, pady=10)

text_area_response = tk.Text(window)
text_area_response.pack(padx=20, pady=10)

text_area_request.bind("<Return>", send_request)

window.mainloop()