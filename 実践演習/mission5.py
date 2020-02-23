from random import randint
hero_hp = 100
maou_hp = 100
print("魔王が現れた\n")

while True: # 戦闘ループ開始
    print("勇者の残りHP" + str(hero_hp) + "\t魔王の残りHP：" + str(maou_hp))
    print("1.こうげき 2.ひっさつ")
    hero_attack = randint(10, 20) # 勇者の今回の攻撃
    select = int(input()) # プレイヤーが選択肢を入力

    # プレイヤーの選択が1の場合
    if select == 1:
        print("勇者の攻撃")
        print("魔王に" + str(hero_attack) + "のダメージを与えた")
        maou_hp -= hero_attack

    # プレイヤーの選択が2の場合
    elif select == 2:
        hit = randint(0, 1) # 勇者のひっさつの命中判定
        print("勇者のひっさつこうげき！")
        if hit == 0: # 攻撃が外れた場合
            print("ミス！")
        else: # 攻撃が命中した場合
            hissatsu = hero_attack * 2 # 勇者の攻撃力を2倍
            print("魔王に" + str(hissatsu) + "のダメージを与えた")
            maou_hp -= hissatsu

    if maou_hp <= 0:
        print("魔王を倒した！\n")
        break
    else:
        maou_attack = randint(10, 20)
        print("魔王の攻撃")
        print("勇者は" + str(maou_attack) + "のダメージを受けた\n")
        hero_hp -= maou_attack
        if hero_hp <= 0:
            print("あなたはしにました\n")
            break
