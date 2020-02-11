from random import randint # randomint関数をインポート
player_hp = 100 # 勇者の初期HPを設定
maou_hp = 100 # 魔王の初期HPを設定
print("魔王が現れた\n")

while player_hp > 0 and maou_hp > 0: # 戦闘ループ開始
	print("勇者の残りHP" + str(player_hp) + "\t魔王の残りHP：" + str(maou_hp)) # 現在のHPを表示
	player_attack = randint(10, 20) # 勇者の今回の攻撃
	print("勇者の攻撃")
	print("魔王に" + str(player_attack) + "のダメージを与えた")
	maou_hp -= player_attack # 魔王のHPを減算
	if maou_hp <= 0: # 魔王のHPが0以下なら
		print("魔王を倒した！\n")
	else: # 魔王のHPが0よりも大きい場合
		maou_attack = randint(10, 20) # 魔王の今回の攻撃
		print("魔王の攻撃")
		print("勇者は" + str(maou_attack) + "のダメージを受けた\n")
		player_hp -= maou_attack # 勇者のHPを減算
		if player_hp <= 0: # 勇者のHPが0以下なら
			print("あなたはしにました\n")
