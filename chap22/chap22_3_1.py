# ラベル、pack

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("400x300")

#ラベル
label = tk.Label(root, text="Hello World") # ラベルウィジェットに表示したい文字を渡してインスタンスを生成
label.pack() # ラベルウィジェットを配置

root.mainloop()
