#半角文字列の変換　※「使っているときだけ」変換 p91-92
print("We hold these truths ...".upper() )
print("SO IT GOES.".lower() )
print("four score and ...".capitalize() )

#変数で実験すると変数の中身は変わっていない
mand = "This is the way."
print(mand) #そのまま
print(mand.upper() )    #大文字で表示
print(mand.lower() )    #小文字で表示
print(mand) #もう一度そのまま

