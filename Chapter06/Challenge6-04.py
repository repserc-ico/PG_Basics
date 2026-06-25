#文字列を特定の文字を区切りとして分割してリストに入れよう
w3string = "どこで？　だれが？　いつ？"
w3list = []

#区切りとする文字は何にする？(テキストp94)
w3list = w3string.split("　")

print(w3string)
print(w3list)
