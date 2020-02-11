import csv
yamato = {"キャラクター": "大和", "装備1": "46cm三連装砲", "装備2": "15.5cm三連装副砲", "装備3": "零式水上観測機"}

with open("/Users/User/Desktop/python_lessons/mission8.csv",mode="a",newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["キャラクター", "装備1", "装備2", "装備3"])
    writer.writerow(yamato)
