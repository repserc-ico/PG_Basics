def f(x=2): #引数が代入式になっていればオプション引数
    return x ** x

print(f())  #引数を省略した場合
print(f(4)) #引数を指定した場合
