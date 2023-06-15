import tkinter as tk
import mysql.connector

def function_name():

    text_area.delete('1.0', tk.END)

    # MySQLサーバーへの接続情報
    config = {
        'user': 'your_user_name',
        'password': 'your_user_password',
        'host': 'localhost',
        'database': 'your_database_name',
        'raise_on_warnings': True
    }

    # MySQLサーバーへの接続
    try:
        cnx = mysql.connector.connect(**config)
        print('MySQLサーバーへの接続に成功しました。')

        # クエリの実行
        # デフォルトだとタプルで取得する為辞書に変更する
        cursor = cnx.cursor(dictionary=True)
        query = 'SELECT * FROM your_table_name'
        cursor.execute(query)

        recordset = cursor.fetchall()
        
        # 結果をtextareaに表示
        for row in recordset:
            text_area.insert(tk.END, str(row['val']) + "\n")

        # 接続を閉じる
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        text_area.insert(tk.END,'MySQLサーバーへの接続に失敗しました。エラー: {}'.format(err))

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("your window name")

# 受信ボタンを作成
button = tk.Button(window, text="メッセージを送信", command=function_name)
button.pack(padx=20, pady=10)

# テキストエリアを作成
text_area = tk.Text(window)
text_area.pack(padx=20, pady=10)

window.mainloop()