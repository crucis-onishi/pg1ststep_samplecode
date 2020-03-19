# 正誤判定

import tkinter as tk

question = "問題！\n株式会社インプレスR&Dが刊行展開している、技術系商業書籍のシリーズ名は次のうちどれ？"
choices = ["技術の泉シリーズ", "技術の庭シリーズ", "技術の山シリーズ", "技術の草原シリーズ"]
answer = "技術の泉シリーズ"

# tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack()
        self.create_widgets()

    # create_widgetsメソッドを定義
    def create_widgets(self):

        # ラベル
        self.label = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, text=question, font=("游ゴシック体", "20", "bold"), bg="white")
        self.label.pack()

        # 選択肢ボタン
        self.buttons = []
        for choice in choices:
            button = tk.Button(self, width=28, text=choice, font=("游ゴシック体", "20", "bold"), command=self.button_clicked(choice))
            button.pack()
            self.buttons.append(button)

    # 選択肢ボタンが押された時の処理（正誤判定）
    def button_clicked(self, choice):
        def x():
            if choice == answer:
                self.label["text"] = "正解！"
            else:
                self.label["text"] = "不正解！"
        return x

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
