#チャレンジ１〜５で作成した関数のDocStringを表示してみるサンプル
#一番最後の行のhelp()に、DocStringを表示したい関数名を指定します
#「q」を入力すると表示を終了します

def kariert(x):
    """
    関数名: kariert
    引数名: x データ型: int
    戻り値: xを2乗した値
    """
    return x ** 2
#関数kariertの記述はここで終わり

def parroting(s):
    """
    関数名: psrroting
    引数名: s データ型: str
    戻り値: sの値そのまま
    備　考: 文字列をオウム返しにしてるからparrotingと名付けた
    """
    print(s)
#ここで関数parrotingのは記述は終わり

def penta(a, b, c, x=3, y=5):
    """
    関数名: penta
    引数名: a : データ型: int : 必須引数 
    引数名: b : データ型: int : 必須引数 
    引数名: c : データ型: int : 必須引数 
    引数名: x : データ型: int : オプション引数(未指定の場合3を代入) 
    引数名: y : データ型: int : オプション引数(未指定の場合5を代入)
    戻り値: なし
    備　考: 引数が5つあるからギリシャ語の５を関数名にした
    """
    print(a)
    print(b)
    print(c)
    print(x)
    print(y)
    return
#ここで関数pentaのは記述は終わり

def func1(x):
    """
    関数名: func1
    引数名: x : データ型: int 
    戻り値: 引数を２で割った数
    備　考: 関数その１ function 1 を略して命名
    """
    return x / 2
#ここで関数func1のは記述は終わり

def func2(y):
    """
    関数名: func2
    引数名: y : データ型: int 
    戻り値: 引数に４をかけた数
    備　考: 関数その２ function 2 を略して命名
    """
    return y * 4
#ここで関数func2のは記述は終わり

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

help(kariert)
