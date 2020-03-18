# after

import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack() # フレームを配置
        self.create_widget() # 下記で定義しているcreate_widgetメソッドを実行

    # create_widgetメソッドを定義
    def create_widget(self):

        # 背景画像
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()
        self.bg_img = tk.PhotoImage(file="haikei.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        self.canvas.create_image(400, 300, image=self.bg_img)

        # ラベル1
        self.label1 = tk.Label(self, relief=tk.RIDGE, width=28, height=1, anchor=tk.N, text="テキスト", font=("游ゴシック体", "20", "bold"), bg="white")
        self.label1.place(x=10, y=10)

        # ラベル2
        self.label2 = tk.Label(self, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, text="テキスト", font=("游ゴシック体", "20", "bold"), bg="white")
        self.label2.place(x=10, y=60)

        # ボタン
        self.button = tk.Button(self, width=28, text="「スイッチ」を押させるなーーーーッ", font=("游ゴシック体", "20", "bold"), bg="white", command=self.button_clicked)
        self.button.place(x=10, y=350)

    # buttonをクリックした時の処理
    def button_clicked(self):
        # self.button["state"] = tk.DISABLED
        self.button["text"] = "びろ～～～ん"
        self.button.after(1000, self.destroy_button)

    # ボタンを削除する処理
    def destroy_button(self):
        self.button.destroy()

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
