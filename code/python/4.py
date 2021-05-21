# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:17:52 2019
独学プログラマー 9章から
@author: ell_Sub2
"""

"""
ファイルを開くには: open([path], [mode], encoding=[encoding])
:param mode: 
    r
    w(上書きされる、ファイルがなければ自動作成)
    w+(読み書き、ファイルがなければ自動作成)  
:param encoding:
    日本語を扱う場合は'utf-8'を指定すべきです。
    ちなみにshift-jisなら'cp932'
:return: file object.
"""
f = open('piyo.txt', 'w+')
f.write('piyopiyo')
print(f.read()) #なぜ表示されない?
f.close()

"""
withで開くと便利
with open([path], [mode]) as [変数名]:
"""
with open('st.txt', 'w') as f:
    f.write('maaaaaaaaaan')

with open('st.txt', 'r') as f:
    print(f.read()) #表示されるやん。ってことはw+やとreadできへんのか?
                    #ちなみに、read()は一度のみできる。もう一回やりたいならもう一回open()

txt = []
with open('st.txt') as f:
    txt.append(f.read()) #すごいべんり。forとか使わんでいいんや...
    
print(txt)

import csv
with open('st.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',') #fはファイルオブジェクト。csv.writer()でcsvオブジェクトを返す
    w.writerow(['one', 'two', 'three']) #write(書く) row(横)
    w.writerow(['four', 'five', 'six'])

#9章チャレンジ
lis = []
with open('1.py', 'r', encoding='utf-8') as f:
     lis.append(f.read())
     
for s in lis:
    print(s)
    
answer = input('Would you like a Lipton Milk Tea?')
with open('ans.txt', 'w', encoding='utf-8') as f:
    f.write(answer)

lislis = [['とっぷがん', '闇ビジネス', 'Minority Report'],
          ['Titanic', 'The Revenant', 'Inception'],
          ['Training day', 'Man on Fire', 'Flight']]

with open('ch3.csv', 'w', newline='') as f:
    c = csv.writer(f, delimiter=',')
    for lis in lislis:
        c.writerow(lis) #なんか間に一行余分な空白が挟まれる
                        #open()でnewline=''を指定すればうまくいくようだ

#9章終わり