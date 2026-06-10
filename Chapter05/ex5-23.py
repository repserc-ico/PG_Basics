#リストを入れるリストを作る
lists = []
#listsの中に入れるリストを用意する
rap = ["カニエ・ウェスト", "ジェイ・z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]
#listsの中に各リストをappendしていく
lists.append(rap)
lists.append(rock)
lists.append(djs)
#listsを表示
print(lists)
#listsのインデックス番号ゼロ番目の要素をrapsに入れる
raps = lists[0]
print(raps)   #print(lists[0])と同じ
#rapsに要素を追加
raps.append("ケンドリック・ラマー")
print(raps)
#lists全体を表示
print(lists)

