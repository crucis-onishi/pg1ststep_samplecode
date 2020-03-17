# キャンバス

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")
root.geometry("400x300")

# canvasウィジェットを作成
canvas = tk.Canvas(root, width=300, height=200, bg="yellowgreen")
canvas.pack()

root.mainloop()
