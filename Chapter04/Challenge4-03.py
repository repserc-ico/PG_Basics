def foo(a,b,c,x=3,y=5):
    q=int(a+b+c*x/y)
    print(q)

l=int(input("数字を入力してください"))
m=int(input("別の数字を入力してください"))
n=int(input("さらに別の数字を入力してください"))
foo(l,m,n)
