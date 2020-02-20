# 各モジュールをインポート
from time import time
from random import choice

words = ["りんご", "ばなな", "みかん", "ぶどう", "もも", "なし", "めろん", "さくらんぼ", "きうい", "いちご"]

score = 0 # score変数を定義

print("ゲームスタート！")
start = time() # プログラム実行開始時の時刻をstart変数に代入

# プログラム開始時からの経過時間が10秒以下の場合はループ
while time() - start <= 10:
    word = choice(words) # wordsリストからランダムに要素を選択してword変数に代入
    print(word) # 選択した要素を表示
    entry = input() # 標準入力から受け取った文字列をentry変数に代入
    if word == entry: # 選択された要素と入力された文字列が一致した場合
        print("OK!\n")
        score += 1
    else: # 選択された要素と入力された文字列が不一致の場合
        print("miss!\n")

print("時間です！")
print("あなたのスコアは" + str(score) + "点です！")
