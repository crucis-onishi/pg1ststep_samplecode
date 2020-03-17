# ウィンドウを配置
# ウィンドウのタイトル
# ウィンドウの幅、高さ

import tkinter as tk # tkinterモジュールを読み込みtkという名前で使えるように

root = tk.Tk() # rootインスタンスを作成

# ウィンドウの設定
root.title("ウィンドウのタイトル") # ウィンドウのタイトルを指定
root.geometry("400x300") # ウィンドウサイズの指定

root.mainloop() # rootインスタンスのmainloopメソッドを呼び出し
