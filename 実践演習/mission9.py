import csv

# ファイルを読み込んで1行目をキー、各行を値とする辞書としてstudent_scoresに代入
with open("/Users/User/Desktop/python_lessons/mission9.csv",newline="",encoding="utf-8") as f:
    dict = csv.DictReader(f)
    students_scores = [row for row in dict]

"""
print(students_scores)
[OrderedDict([('生徒名', '秋原'), ('国語', '30'), ('数学', '40'), ('英語', '50')]),
 OrderedDict([('生徒名', '今井'), ('国語', '60'), ('数学', '60'), ('英語', '60')]),
 OrderedDict([('生徒名', '上田'), ('国語', '80'), ('数学', '20'), ('英語', '40')]),
（以下略）
"""

# 必要な変数、辞書、リストを定義
total = 0
average = 0
new_dict = {}
new_list = []

# 読み込んだCSVファイルを元に新たな表データ(new_list)を作成
for row in students_scores: # 表データから1行ずつ取得（生徒ごとのデータ）
    total = int(row["国語"]) + int(row["数学"]) + int(row["英語"]) # 合計点を計算してtotal変数に代入
    average = int(total / 3) # 平均点を計算してaverage変数に代入
    new_dict = {"生徒名":row["生徒名"], "国語":row["国語"], "数学":row["数学"], "英語":row["英語"], "合計点":total, "平均点":average} # 新たな辞書（生徒ごとのデータ）を作成
    new_list.append(new_dict) # 生徒ごとのデータを1つの要素として新たな表データ（多次元リスト）に追加

"""
print(new_list)
[{'生徒名': '秋原', '国語': '30', '数学': '40', '英語': '50', '合計点': 120, '平均点': 40},
 {'生徒名': '今井', '国語': '60', '数学': '60', '英語': '60', '合計点': 180, '平均点': 60},
  {'生徒名': '上田', '国語': '80', '数学': '20', '英語': '40', '合計点': 140, '平均点': 46},
（以下略）
"""

# 新たな表データ(new_list)を新規作成したCSVファイルに書き込み
with open("/Users/User/Desktop/python_lessons/mission9ans.csv",mode="w",newline="",encoding="utf-8") as f:
    fieldname = ["生徒名", "国語", "数学", "英語", "合計点", "平均点"]
    writer = csv.DictWriter(f, fieldname) # 書き込み用として読み込み、キーを指定
    writer.writeheader() # ヘッダー（見出し行）を書き込み
    for row in new_list: # new_listの各行にあたる各生徒の辞書データを順に取得
        writer.writerow(row) # 辞書を書き込み
