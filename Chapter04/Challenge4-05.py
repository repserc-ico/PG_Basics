def turnf(x):
    return float(x)

try:
    i=input("なにか入力してください")
    print(turnf(i))
except(ValueError):
    print("数字ではないので処理を中止します")
