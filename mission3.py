flag = False
while flag == False:
    print("問題：この本のタイトルはなんでしょう？")
    print("1.Pythonの教科書")
    print("2.ゼロから学ぶPython")
    print("3.Python3で学ぶプログラミング入門")
    ans = int(input("答えは？"))
    if ans == 3:
        print("正解！\n")
        flag = True
    else:
        print("残念！\n")

flag = False
while flag == False:
    print("問題：次のうちPythonに当てはまるのは？")
    print("1.静的型付け言語")
    print("2.動的型付け言語")
    print("3.俺的カッコ付け言語")
    ans = int(input("答えは？"))
    if ans == 2:
        print("正解！\n")
        flag = True
    else:
        print("残念！\n")

flag = False
while flag == False:
    print("問題：次のうちPythonに当てはまるのは？")
    print("1.コードがシンプルで扱いやすい汎用言語")
    print("2.国産のプログラミング言語")
    print("3.HTMLに埋め込んで使うことができるWeb開発に適した言語")
    ans = int(input("答えは？"))
    if ans == 1:
        print("正解！\n")
        flag = True
    else:
        print("残念！\n")
