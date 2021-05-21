# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:38:02 2019
独学プログラマー第一部5章から
@author: ell_Sub2
"""

#Method
print('hello, world'.upper()) #upper method.
print('hello, world'.replace('o', '@')) #methodはオブジェクトに対しての操作
                                        #'hello, world'はオブジェクト
            
###############################
#LIST
###############################                 
#List:順番にオブジェクトを保存するコンテナ
#[List_name] = [obj1, obj2, obj3, ...]
fluit = list() #fluitは[]を返す。これがList
#若しくはfluit = []と書く

#Listはイテラブル(繰り返し可能)、ミュータブル(変更(オブジェクトの追加、削除、順番変更)可能)
vegetables = ['pi-man', 'cabetz', 'go-ya']
vegetables.append('gorila')
vegetables[2] = 'negi'
print(vegetables.pop()) #'gorila'(末尾のオブジェクト)を取り出し、同時に消す=popする
if 'negi' in vegetables: #in:オブジェクトがリストに含まれているかどうか調べる演算子、逆:not in
    print('negi is vegetable.')
print(vegetables)


###############################
#Tuple
###############################
#イテラブル、イミュータブル(変更不能)
my_tuple = () #タプルは()で召喚する
my_tuple = ('M. jack', 1958, True)
#要素が一つだけの場合は(10,)とすること。しないと(10)と見なされる(算術演算の())
#my_tuple.append(10) #アカンできへん
#タプルは、ミュータブルであってほしくないオブジェクトに使う。不変であることを保証してくれる頼もしい味方だ。


###############################
#Dictionary(辞書型)
#KeyでValueを取り出せるやーつ。逆は無理。
###############################
#順番不明(Python3.7からは固定らしい)、Valueはミュータブル、Keyはイミュータブル
#従って、文字列かタプルがKeyに使用できる。
fluits = {'Apple':'Red',
         'Banana':'Yellow'} #{}ｷﾀ━━━━(ﾟ∀ﾟ)━━━━!!

#アクセス方法
print(fluits['Apple'])
fluits['Lemmon'] = ['米津玄師']

print('Lemmon' in fluits)
print('米津玄師' in fluits) #Valueはin演算子で確認できない

del fluits['Lemmon'] #バイバイ玄師...
print(fluits)

songs = {'1':'fun',
         '2':'blue',
         '3':'me',
         '4':'floor',
         '5':'live'}

n = input('数字を入力してください')
if n in songs:
    song = songs[n]
    print(song)
else:
    print('見つからないよ!')
    
#5章チャレンジ
#fav_museans = ["初音ミク", "鏡音リン", "タコ"]
my_featurs = {'height':175, 'weight':70, 'fav':'bike'}
d = input('please input somethings of Key:')
if d in my_featurs:
    print(my_featurs[d])
else:
    print('何も一致しねえ...')
    
fav_museans = {"初音ミク":["初めての恋が終わる時","メルト","夕日坂"],
               "鏡音リン":["リンちゃんなう"],
               "タコ":["ルカルカ★ナイトフィーバー"]}

#Pythonのset型:集合を表現する

#5章終わり
