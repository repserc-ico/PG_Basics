#formatによる書式指定を変数に入れてから表示
what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした:")

r = "{}は{}、{}で{}。".format(what, when, where, do)
print(r)
#f文字列を使っての書式指定だとこうなります
print(f"{what}は{when}、{where}で{do}。")
