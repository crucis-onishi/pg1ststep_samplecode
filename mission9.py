import csv

with open("/Users/User/Desktop/python_lessons/mission9.csv",newline="",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    dict = [row for row in reader]

dict[0]["装備1"] = "烈風"

with open("/Users/User/Desktop/python_lessons/mission9.csv",mode="w",newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["キャラクター", "装備1", "装備2", "装備3"])
    writer.writeheader()
    writer.writerows(dict)
