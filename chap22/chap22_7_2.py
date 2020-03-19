# ウィジェットの張り替え

import tkinter as tk
from random import randint

# tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack()
        self.button = tk.Button(self, width=20, text="ゲームスタート！", font=("游ゴシック体", "20", "bold"), bg="white", command=self.recreate_button)
        self.button.place(x=200, y=250)

    # recreate_buttonメソッドを定義
    def recreate_button(self):

        self.button.destroy() # 既存のボタンを削除

        x = randint(0, 700) # X座標を0から700までの間でランダムに取得
        y = randint(0, 540) # Y座標を0から540までの間でランダムに取得

        # 新しいボタンを生成・配置
        self.button = tk.Button(self, width=5, text="ここ！", font=("游ゴシック体", "20", "bold"), bg="white", command=self.recreate_button)
        self.button.place(x=x, y=y)

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
