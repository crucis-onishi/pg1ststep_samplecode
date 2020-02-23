import csv

# ファイルを読み込んで1行目をキー、各行を値とする辞書としてstudent_scoresに代入
with open("/Users/User/Desktop/python_lessons/mission8.csv"
,newline="",encoding="utf-8") as f:
    dict =  csv.DictReader(f)
    students_scores = [row for row in dict]

# 必要な変数を定義
king = ""
best_score = 0

# 点数が1位の生徒を判定
for row in students_scores: # 表データの行を1つずつ取得
    if best_score < int(row["点数"]): # 点数がbest_score変数よりも大きければ
        best_score = int(row["点数"]) # 点数をbest_score変数に代入
        king = row["生徒名"] # その点数の生徒の名前をking変数に代入

# ループで全ての生徒の点数を比較した後、結果発表
print(king + "くんが" + str(best_score) + "点で1位でした！")
