# ボタン

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("400x300")

#ボタン
button = tk.Button(root, text="Click me!", font=("游ゴシック体", "20", "bold")) # ボタンに表示したい文字を渡してインスタンスを生成
button.place(x=100, y=100) # インスタンスのplaceメソッドを実行

root.mainloop()
