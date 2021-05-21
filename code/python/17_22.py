# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:17:08 2019
独学プログラマー 第22章
@author: ell_Sub2
"""
import time

#フィズバズ
def fizzz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        
        time.sleep(1)

#線形探索
def liner_search(lis, purpose):
    """
    :param lis: リスト形式
    :param paurpose: 目的のオブジェクト。例えば、"hoge"、1、 1.5
    :return: 存在すればTrue、存在しなければFalse
    """
    for l in lis:
        if l == purpose:
            return True
        else:
            continue
        
    return False
    
#nums = range(0, 100)
#s = liner_search(nums, 1000)
#print(s)
    
#回文
def palindrome(word):
    word = word.lower()
    return word[::-1] == word #[開始:終了:ステップ]

#print( palindrome("たけやぶやけろ") )

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

#print( anagram("hoge", "hego") )
 
#文字列を1文字づつループ
#文字の出現回数を辞書に記録する
def hoge(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 0
        dic[c] += 1
    
    return dic

print(hoge("Explicit is better than implicit."))