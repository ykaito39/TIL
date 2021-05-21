# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 07:27:35 2019
独学プログラマー6章から
@author: ell_Sub2
"""

author = 'ell_sub2'
print(author.upper()) #逆はlower
print(author.capitalize()) #先頭文字のみを大文字に

print("こんにちは、{}".format('世界!')) #format()は、strオブジェクト中の{}に引数を差し込む

"""
#formatの有用な使い方の例
what = input('何が:')
when = input('いつ:')
where = input('どこで:')
do = input('何をした:')

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)
"""

s = 'はやぶさがイトカワに到着した。すごかったんだぜ!'
print(s.split('。')) #分割
#print(s)
print('+'.join(s)) #オブジェクトを、引数に与えたオブジェクトの(すべての)間に挟む

words = ['The', 'fox', 'jumped',
         'over', 'the', 'fence', '.']
one = ' '.join(words)
print(one)

s = '   俺が―――王だ。   '
s = s.strip() #意訳:脱ぐ "文字列の"最初と最後の空白を除く
print(s)

s = s.replace('俺が','お前が') #置き換え
print(s)

try:
    s.index('の') #index()で、文字が最初に現れる位置をす取得できる。
except:
    print('Not found \'の\'')
    
if '王' in s: #単純に文字列を含むかどうかを調べるにはこうする
    print('王は文字列sに含まれる。')
    
#6章チャレンジ
def ch6_1():
    for s in "カミュ": #注意inの前後
        print(s)
    
def ch6_2():
    s1 = input("1文字目:")
    s2 = input("2文字目:")
    print("私は昨日{}を書いて、{}に送った!".format(s1,s2))

def ch6_3(s = "aldous Huxley was born in 1894."):
    print(s.capitalize())
ch6_3()

s = 'どこで? 誰が? いつ?'
print(s.split(' '))

#print(" ".join(words[:-1]) + words[-1]) #僕の回答

#公式の回答
fox = " ".join(words)
fox = fox[0:-2] + "." #こっちのほうがわかりやすいな
print(fox)

########6章終わり########

"""
書式
for [変数名] in [イテラブル]:
    [ブロック]
:param[イテラブル]:取り出し元。
:param[変数名]:イテラブルから取り出したものを代入する。
"""

showes = ('GOT', 'Narcos', 'Vice') #タプルはイミュータブルであるが、イテラブルである。文字列も同様
for show in showes:
    print(show)

people = {'G. Blith II': 'A Development',
          'Barney': 'HIMYM',
          'Dennis': 'Always Sunny'}
for ch in people: #取り出されるのはKey
    print(ch)
    print(people[ch]) #Valueがほしいならこうすれば良い

tv = ('GOT', 'Narcos', 'Vice')
for i, new in enumerate(tv): #インデックス値iと、tv内のオブジェクトnewを取得できる
    print(new)               #ループ用変数を自分で明示的にわざわざ作る必要がない

tv = ['GOT', 'Narcos', 'Vice']
coms = ['Arrested Development', 'friends', 'Always Sunny']
all_shows =[]

for show in tv:
    show = show.upper()#各文字をすべて大文字に
    all_shows.append(show)#別のリストに追加する
    
for show in coms:
    show = show.upper()#各文字をすべて大文字に
    all_shows.append(show)#別のリストに追加する

print(all_shows)

"""
while input('y or n?:') != 'n':
    for i in range(1, 6):
        print(i)
"""

#6章チャレンジ
lis1 = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for s in lis1:
    print(s)

for i in range(25, 51):
    print(i)

for i, s in enumerate(lis1):
    print('{}: {}'.format(i, s))


""" #つまづき申した。
correct = [1, 2, 4, 6, 8, 10]
while True:
    n = input('Enter a number:')
    if n == 'q': break;
    try:
        if int(n) in correct:
            print('正解')
        else:
            print('不正解')
    except:
        print('数字を入力するか、qで終了します')
"""


lis1 = [8, 19, 148, 4]
lis2 = [9, 1, 33, 83]
ans = []
for i in lis1:
    for j in lis2:
        ans.append(i*j)
print(ans)

############7章終了############

import math
import random

print(math.pow(2, 3))
print(random.randint(0, 10))

#次はtestpディレクトリ内