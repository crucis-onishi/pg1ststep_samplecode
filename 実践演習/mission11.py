import csv,random # モジュールをインポート

# cradクラスを定義
class card:
    def __init__(self,rarity,name,type):
        self.rarity = rarity
        self.name = name
        self.type = type
    def msg(self):
        return self.type + self.name + "、着任しました！" + "レアリティは" + self.rarity + "です！"

 # ランダムな整数を取得、その数に応じて入手カードを決める
gacha = random.randint(1,6)

if gacha == 1:
    number = 1
elif gacha <= 3:
    number = 2
else:
    number = 3

# ガチャの結果に基づいたデータをCSVから取得
with open("/Users/User/Desktop/python_lessons/mission10.csv",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)
    list = [row for row in reader]

# 取得したデータからオブジェクトを生成、msgメソッドを実行
get = card(list[number][0],list[number][1],list[number][2])
print(get.msg())
