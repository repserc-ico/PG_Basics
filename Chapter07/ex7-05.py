#ループでリストの要素ひとつひとつを大文字に変換する
tv = ["GOT","Narcos","Vice"]
i = 0
for show in tv:
    tv[i] = show.upper()
    i += 1

print(tv)
