import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        print(index)
        listbox.delete(index)
    except:
        pass

root = tk.Tk()
root.title("ToDoリスト")

frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=50, height=10, bd=0, font=("Courier New", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Courier New", 12))
entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="追加", command=add_task)
add_button.grid(row=0, column=0)

delete_button = tk.Button(button_frame, text="削除", command=delete_task)
delete_button.grid(row=0, column=1)

root.mainloop()
