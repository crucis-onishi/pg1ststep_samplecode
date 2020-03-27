# 複数のボタンのうちどれが押されたかを判定

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("600x300")

# buttonをクリックした時の処理
def button_clicked(item):
    label["text"] = "あなたが押したボタンは　" + item

# labelウィジェットを生成・配置
label = tk.Label(root,text="あなたが押したボタンは　ほにゃらら", font=("游ゴシック体", "20", "bold"))
label.place(x=50, y=30)

# ボタン
items = ["あいうえお","かきくけこ","さしすせそ"]

for i,item in enumerate(items):
    button = tk.Button(root, width=28, text=item, font=("游ゴシック体", "20", "bold"), bg="white", command=button_clicked(item))
    button.place(x=50, y=100 + (i * 60))

root.mainloop()
