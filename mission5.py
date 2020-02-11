from random import randint
player_hp = 100
maou_hp = 100
print("魔王が現れた\n")

while player_hp > 0 and maou_hp > 0:
	print("勇者の残りHP" + str(player_hp) + "\t魔王の残りHP：" + str(maou_hp))
	print("1.こうげき 2.ひっさつ")
	player_attack = randint(10, 20) # 勇者の今回の攻撃
	select = int(input()) # プレイヤーが選択肢を入力
	if select == 1: # プレイヤーの選択が1の場合
		print("勇者の攻撃")
		print("魔王に" + str(player_attack) + "のダメージを与えた")
		maou_hp -= player_attack
	elif select == 2: # プレイヤーの選択が2の場合
		hit = randint(0, 1) # 勇者のひっさつの命中判定
		print("勇者のひっさつこうげき！")
		if hit == 0: # 攻撃が外れた場合
			print("ミス！")
		else: # 攻撃が命中した場合
			hissatsu = player_attack * 2 # 勇者の攻撃力を2倍
			print("魔王に" + str(hissatsu) + "のダメージを与えた")
			maou_hp -= hissatsu
	if maou_hp <= 0:
		print("魔王を倒した！\n")
	else:
		maou_attack = randint(10, 20)
		print("魔王の攻撃")
		print("勇者は" + str(maou_attack) + "のダメージを受けた\n")
		player_hp -= maou_attack
		if player_hp <= 0:
			print("あなたはしにました\n")
