def expon(x):
    """
    引数の累乗を返す関数:
    :param x: intが望ましい
    """
    return x**2

def parroting(s):
    """
    引数をおうむ返しする関数
    :param s: 数字でも文字列のどちらでもよい
    """
    print(s)

def foo(a,b,c,x=3,y=5):
    """
    必須引数を足してオプション引数でかけたり割ったりする関数
    :param a: 必須引数。intが望ましい  
    :param b: 必須引数。intが望ましい  
    :param c: 必須引数。intが望ましい  
    :param x: オプション引数。これをかける  
    :param y: オプション引数。これで割る  
    """
    q=int(a+b+c*x/y)
    print(q)

def func1(x):
    """
    引数を半分にする関数
    :param x: intが望ましい
    """
    return int(x/2)

def func2(y):
    """
    引数を４倍する関数
    :param y: intが望ましい
    """
    return int(y*4)

def turnf(x):
    """
    引数をfloat型にする関数
    :param x: 文字を入れるとValueErrorが発生する
    """
    return float(x)

