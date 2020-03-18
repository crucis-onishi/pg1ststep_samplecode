# PhotoImage、create_image

import tkinter as tk

root = tk.Tk()

# ウィンドウの設定
root.title("ウィンドウのタイトル")

# canvasウィジェットを生成・配置
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

img = tk.PhotoImage(file="haikei.png") # 画像ファイルを読み込んでimgオブジェクトを生成
canvas.create_image(400, 300, image=img) # 画像ファイルを描画

root.mainloop()
