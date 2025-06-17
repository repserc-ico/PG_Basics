tv=["GOT", "Narcos", "Vice"]
i=0

for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i]=new
    i+=1
"""↑の繰り返し処理がどうなっているか
    new = tv[0]
    new = new.upper()
    tv[0]=new
    new = tv[1]
    new = new.upper()
    tv[1]=new
    new = tv[2]
    new = new.upper()
    tv[2]=new
"""

print(tv)

