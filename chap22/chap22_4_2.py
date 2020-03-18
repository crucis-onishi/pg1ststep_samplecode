# command

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("600x300")

# buttonをクリックした時の処理
def button_clicked():
    button["text"] = "びろ～～～ん" # buttonインスタンスのtextを書き換え

# labelウィジェットを生成・配置
label = tk.Label(root,text="「スイッチ」を押させるなーーーーッ", font=("游ゴシック体", "20", "bold"))
label.place(x=50, y=30)

#buttonウィジェットを生成・配置
button = tk.Button(root, text="いいや！限界だ押すね！", font=("游ゴシック体", "20", "bold"), command=button_clicked) # command引数に関数を指定
button.place(x=100, y=120)

root.mainloop()
