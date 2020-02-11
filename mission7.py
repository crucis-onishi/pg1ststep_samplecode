with open("/Users/User/Desktop/python_lessons/mission7.txt"
,encoding="utf-8") as f:
    list = [s.strip() for s in f.readlines()]

king = ""
score = 0

for i in list:
    members = i.split(",")
    if score < int(members[1]):
        score = int(members[1])
        king = members[0]
print(king + "くんが" + str(score) + "点で1位でした！")