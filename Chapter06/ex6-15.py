#文字列の中で該当する特定の文字を全て置き換える
equ = "All animals are equal."
equ = equ.replace("a","@")
print(equ)

#特定文字が一文字だけなら一文字だけ置き換えも可能
author = "Kafka"
author = author.replace("f","v")
print(author)
