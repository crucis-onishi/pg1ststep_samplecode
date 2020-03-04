import csv # csvモジュールをインポート

# cradクラスを定義
class card:
    # コンストラクタを定義
    def __init__(self,rarity,name,type):
        self.rarity = rarity
        self.name = name
        self.type = type
    # msgメソッドを定義
    def msg(self):
        return self.type + self.name + "、着任しました！" + "レアリティは" + self.rarity + "です！"

# データをCSVから取得
with open("/Users/User/Desktop/python_lessons/mission10.csv",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)
    list = [row for row in reader] # 2次元リストに変換

kongou = card(list[2][0],list[2][1],list[2][2]) # 該当するデータからオブジェクトを生成
print(kongou.msg()) # メソッドを実行
