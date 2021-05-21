# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:21:23 2019
独学プログラマー 17章 正規表現ライブラリの練習
@author: ell_Sub2
"""

import re

"""
正規表現:
    .   どんな文字にも一致
    ^   行の先頭のみを対象
    $   行の終端のみを対象
    *   直前のパターンが0回以上繰り返すものに一致
    []  この中のどれかに一致:[abc] abcのどれか
        "two too"で"t[wo]oなら['two', 'too']が得られる
    \d  数字に一致(連続していてもおk)
    .*  どんな文字"列"にも一致(.だけなら文字にしか一致しない)
    __. *__は貪欲
        __で繋がってたら、最後まで一致してしまう
        非貪欲(最初の1つだけ)にするには__.*?__
        grepでは使えないよ
    \\$ エスケープの書き方
第三引数:
    re.IGNORECASE -> 大文字小文字無視
    re.MULTILINE -> 複数行のテキストを扱う
"""


#l = "Beautiful is better than ugly"
#
#zen = """The Zen of Python, by Tim Peters
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!
#"""
#
#m = re.findall("^[BES]", zen, re.MULTILINE)
#print(m)


#Mab Libsゲーム

text = """キリンは大昔から __複数名詞__ の興味の対象でした。キ
リンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのよ
うな長い __体の一部__ をどうやって獲得したのか説明できません。キリン
の身長は __数値__ __単位__ 近くあり、その高さの殆どは足と __体の一部__ 
によるものです。
"""

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None: #mlsに__ __が含まれていない場合の対策?
        for word in hints:
            input_data = input("{}を入力".format(word))
            mls = mls.replace(word, input_data)
        print('\n')
        mls = mls.replace('\n', '')
        print(mls)
    else:
        print("mlsが無効です")

#チャレンジ3
mozi = "hoge foo ghost, loo"
m = re.findall(".oo", mozi)
print(m)