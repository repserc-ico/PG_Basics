import random

fortune=["大吉","中吉","中吉","小吉","小吉","吉","吉","吉","吉","凶"]
kekka=random.choice(fortune)
print(kekka)


#---こんな書き方もある---
dai="大吉"  #1
tyu="中吉"  #2 3
syo="小吉"  #4 5
kiti="吉"   #6 7 8 9 
kyou="凶"   #10
r=random.randint(1,10)
if r==1:
    kekka=dai
if r==2 or r==3:
    kekka=tyu
if r==4 or r==5:
    kekka=syo
if r==6 or r==7 or r==8 or r==9:
    kekka=kiti
if r==10:
    kekka=kyou

print(kekka)

##-----------------------

import random

fortune=["大吉","中吉","小吉","吉","凶"]
r=random.randint(1,1000)

if r<=100:
    kekka=fortune[0]
elif r>150 and r<=400:    # 100 < r <=350
    kekka=fortune[1]
elif r>400 and r<=500:    # 350 < r <=500
    kekka=fortune[2]
elif r>500 and r<=900:    # 500 < r <=900
    kekka=fortune[3]
else:
    kekka=fortune[4]

print(kekka)


##------------------

import random

fortune=["大吉","中吉","小吉","吉","凶"]    #おみくじの結果
rate=[0,150,400,550,950]    #おみくじの出る範囲の調整
r=random.randint(1,1000)

if r<=rate[0]:
    kekka=fortune[0]
if r>rate[0] and r<=rate[1]:
    kekka=fortune[1]
if r>rate[1] and r<=rate[2]:
    kekka=fortune[2]
if r>rate[3] and r<=rate[4]:
    kekka=fortune[3]
if r>rate[4]:
    kekka=fortune[4]

print(kekka)


