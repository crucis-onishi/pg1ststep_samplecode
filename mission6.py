with open("/Users/User/Desktop/python_lessons/mission6.txt",encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]

if len(l[0]) > len(l[1]):
    print(l[0])
elif len(l[0]) < len(l[1]):
    print(l[1])
else:
    print("Same")