#formatメソッドによる書式指定
print("こんにちは{}".format("ウィリアム・フォークナー") )
name = "ウィリアム・フォークナー"
print("こんにちは{}".format(name) )
#formatメソッドには複数の値が指定できる
author = "宮沢賢治"
year_born = "1896"
print("{}は{}年に生まれました。".format(author, year_born) )
#こう書いたほうがスッキリかも？
print(f"{author}は{year_born}年に生まれました。")




