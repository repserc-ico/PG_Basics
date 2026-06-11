#文字列の中の全部のアルファベットを大文字にして表示する
print("Hello".upper() )
#文字列の中の特定の文字を別の文字に入れ替えて表示する
print("Hello".replace('o', '@') )

#メソッドを使っても、変数の中身が入れ替わっているわけではない
string = "CAT"
print(string.lower() )
print(string.replace('C','H') )
print(string)
