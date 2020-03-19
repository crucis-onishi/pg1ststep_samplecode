# bindメソッドを使わずcommandでやるパターン（callback関数にテキストを渡す）

import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("クイズPythonアカデミー")

        # クイズの問題文、選択肢、正解のテキストを定義
        self.questions = [
                        {"問題文":"株式会社インプレスR&Dが刊行展開している、技術系商業書籍のシリーズ名は次のうちどれ？",
                            "選択肢":["技術の庭シリーズ", "技術の山シリーズ", "技術の泉シリーズ", "技術の草原シリーズ"],
                            "正解":"技術の泉シリーズ"},
                        {"問題文":"次のうちPythonに当てはまるのは？",
                            "選択肢":["静的型付け言語", "動的型付け言語", "オレ的カッコつけ言語"],
                            "正解":"動的型付け言語"},
                        {"問題文":"次のうちPythonに当てはまるのは？",
                            "選択肢":["シンプルで扱いやすい汎用言語", "国産のプログラミング言語", "マークアップ言語の1つ", "ブラウザ上で動作するスクリプト言語"],
                            "正解":"シンプルで扱いやすい汎用言語"}
                    ]

        # 変数定義
        self.question_number = 0 # 現在が何問目かのカウント
        self.score = 0.00 # ユーザーの現在までの得点
        self.allocate_points = 100 / len(self.questions) # 1問当たりの配点

        # 実行内容
        self.pack()
        self.create_widget()
        self.create_buttons()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 背景画像
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.pack()
        self.bg_img = tk.PhotoImage(file="haikei.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        canvas.create_image(400, 300, image=self.bg_img)

        # 得点版
        self.scoreboard = tk.Label(self, relief=tk.RIDGE, width=17, height=3, text="得点\n" + str(round(self.score, 2)), font=("游ゴシック体", "20", "bold"), bg="white")
        self.scoreboard.place(x=500, y=10)

        # 第〇問
        self.question_number_label = tk.Label(self, relief=tk.RIDGE, width=28, height=1, anchor=tk.N, text="第" + str(self.question_number + 1) + "問", font=("游ゴシック体", "20", "bold"), bg="white")
        self.question_number_label.place(x=10, y=10)

        # 問題文
        self.sentence = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, text=self.questions[self.question_number]["問題文"], font=("游ゴシック体", "20", "bold"), bg="white")
        self.sentence.place(x=10, y=60)

    # create_buttonsメソッドを定義
    def create_buttons(self):
        self.buttons = []
        for i,choice in enumerate(self.questions[self.question_number]["選択肢"]):
            button = tk.Button(self, width=28, text=choice, font=("游ゴシック体", "20", "bold"), bg="white", command=self.button_clicked(choice))
            button.place(x=10, y=350 + (i * 60))
            self.buttons.append(button)

    # create_resultメソッドを定義
    def create_result(self):
        result = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.CENTER, wraplength=470,text="問題は以上です。\nお疲れさまでした。",font=("游ゴシック体", "20", "bold"), bg="white")
        result.place(x=10, y=60)

    # ボタンを全てDISABLEDにする処理
    def button_disabled(self):
        for button in self.buttons:
            button["state"] = tk.DISABLED

    # 選択肢ボタンが押された時の処理（正誤判定）
    def button_clicked(self, choice):
        def x():
            self.button_disabled()
            if choice == self.questions[self.question_number]["正解"]:
                self.sentence["text"] = "正解！"
                self.score += self.allocate_points
                self.scoreboard["text"] = "得点\n" + str(round(self.score, 2))
            else:
                self.sentence["text"] = "不正解！"

            self.after(1500, self.next)
        return x

    # 正解不正解表示後の処理
    def next(self):
        self.question_number += 1
        self.destroy_buttons() # 選択肢ボタンをすべて削除

        if self.question_number < len(self.questions):
            self.question_number_label["text"] = "第" + str(self.question_number + 1) + "問" # 何問目かを更新
            self.sentence["text"] = self.questions[self.question_number]["問題文"] # 問題文を更新
            self.create_buttons() # 次の選択肢ボタンを生成・配置
        else:
            self.question_number_label.destroy()
            self.sentence.destroy()
            self.create_result() # リザルト画面を描画

    # 選択肢ボタンをすべて削除する処理
    def destroy_buttons(self):
        for button in self.buttons:
            button.destroy()

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
