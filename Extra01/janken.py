#最初にrandomモジュールを呼び出す(乱数のため)
import random

#input文で人間側のじゃんけんの手を入力させ、変数に入れる
te=int(input("どの手を出しますか？(1:グー 2:チョキ 3:パー)"))
#乱数でコンピュータ側のじゃんけんの手を決め、変数に入れる
com=random.randint(1,3)


#勝ち負けの判定
if te==1 and com==2:
elif te==1 and com==3:
elif te==2 and com==1:
elif te==2 and com==3:
elif te==3 and com==1:
elif te==3 and com==2:
else:
    #あいこ


if te==com: #あいこ
else #勝ちか負けか
    if te==1:
        if com==2:
        if com==3:
    if te==2:
        if com==1:
        if com==3:
    if te==3:
        if com==1:
        if com==2:



if te==1:
    if com==1:
    if com==2:
    if com==3:

if te==2:
    if com==1:
    if com==2:
    if com==3:

if te==3:
    if com==1:
    if com==2:
    if com==3:


#結果表示
print("あなたの手：{} コンピュータの手：{}",format(te,com))
print("{}",format(result))

