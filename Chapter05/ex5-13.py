#リストcolorsの中に入っている値を当てるクイズ(みたいなもの)
colors = ["purple", "orange", "green", "white", "kahki"]
guess = input("リストに入っている色を当ててください->")

if guess in colors:
    print("当たり！")
else:
    print("残念。外れです")
