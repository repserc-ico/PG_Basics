#文字列型の引数をfloat型に変換した数を戻り値にする関数と、
#その関数を使用した際に発生した例外処理
def float_to(s):
    """
    関数名: float_to
    引数名: s : データ型: str 
    戻り値: 引数をfloat型に変換した値
    備　考: 「float型にする」という意味合いで名付けた
    """
    try:
        return float(s)
    except (ValueError):
        print("数字ではないので処理を中止します")
#ここで関数fload_toのは記述は終わり

#関数float_toに値を指定し、その結果を変数fに代入
f = float_to("")
print(f)
