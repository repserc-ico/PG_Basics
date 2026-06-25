#リストの文字列をひとつの文字列に連結する。最後のピリオドに注意。
fox = ["The","fox","jumped","over","the","fence","."]

#結合のメソッドは何でしたっけ？(テキストp94参照)
string = " ".join(fox)
print(string)
#結合した文字列の最初から、最後から２番めの文字列までを取り出す
#テキストp99-100参照
string2 = string[0:-2]
#取り出した文字列の最後に"."を連結する
print(string2+".")
