from random import randint # randomモジュールをインポート
hands = ["グー", "チョキ", "パー"] # リストを作成

# リザルトメッセージの辞書を作成
result_msg = {"勝ち":"あなたの勝ちです！おめでとー！",
"あいこ":"あいこです。むむむ。",
"負け":"あなたの負けです…"}

# お互いの手の組み合わせをキー、勝敗を値とする辞書を作成
judge = {(0,0):"あいこ",(0,1):"勝ち",(0,2):"負け",
(1,0):"負け",(1,1):"あいこ",(1,2):"勝ち",
(2,0):"勝ち",(2,1):"負け",(2,2):"あいこ"}

print("じゃーんけーん…")

# じゃんけんループ開始
while True:
    cpu_hand = randint(0,2) # CPUの手をランダムに選択

    # 入力が適切かどうかの判定ループ
    while True:
        print("出す手を選んでください")
        player_hand_str = input("0.グー　1.チョキ　2.パー") # プレイヤーが手を入力
        if player_hand_str not in ["0","1","2"]: # プレイヤーの手が0でも1でも2でもない場合
            print("")
            print("0か1か2を入力して手を選択してください")
            print("")
            continue # ループを継続
        else: # プレイヤーの入力が適切な場合
            player_hand = int(player_hand_str) # 取得した値を整数型に変換
            break

    # それぞれの手をhandsリストのインデックス番号としてグーチョキパーの文字列を表示
    print("あなたの手は" + hands[player_hand])
    print("CPUの手は" + hands[cpu_hand])
    print(result_msg[judge[player_hand,cpu_hand]]) # お互いの手の組み合わせからリザルトメッセージを表示

    # あいこの場合のみじゃんけんループを継続
    if player_hand == cpu_hand:
        print("")
        continue
    else:
        break
