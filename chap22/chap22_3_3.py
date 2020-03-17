# ただ配置するだけでなく、位置や文字の大きさを調整してみましょう。
# Labelのオプション引数
# パソコンによって使えるフォントが異なるので注意してください。
# 任意の位置に配置するにはplaceメソッドを使います

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("400x300")

#ラベルウィジェットを生成・配置
label = tk.Label(root, text="Hello World", relief=tk.RIDGE, width=14, height=1, font=("游ゴシック体", "20", "bold"), bg="white")
label.place(x=100, y=100)

root.mainloop()
