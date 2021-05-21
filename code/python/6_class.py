# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:32:10 2019
独学プログラマー 第二部 開始
@author: ell_Sub2
"""

"""
「ステート」
    状態を意味する。
    この本では、変数とほぼ同義として扱われている?
    手続き型のパラダイムでは、(注意して書かなければ)グローバルステートを生み出す。
    グローバルステートが多くなると、所謂スパゲッティコードになってしまう。
    関数型とオブジェクト指向型はこの問題点を解決するために生まれた。
    関数型では、引数と戻り値を使うため、グローバルステートが発生しない。
    ステートは関数内にのみ生じる。
    オブジェクト指向型は、オブジェクトにステートをもたせることで解決した。
「インスタンス」
    クラスから生成されたオブジェクトのこと。~クラスのインスタンス。単にオブジェクトで可。
「リテラル」
    プログラミング言語によって予約されている特殊なインスタンス。
    例えば123はintクラスのインスタンスであり、明示的にnewしてない。これはリテラルであるといえる。
    
class [クラス名]: #クラス名はキャメルケースで
    [スイート]

"""

class Orange:
    def __init__(self, w, c): #selfはメソッドの呼び出し元オブジェクトを表す
        self.weight = w       #通常、インスタンス変数は__init__で定義する
        self.color = c        #__init__で定義された変数のスコープは、class内全体
        self.mold = 0 #たぶん腐り加減
        print("Created!")
    
    def rot(self, days, temp): #オレンジの腐る性質
        """tempはセ氏"""
        self.mold = days * temp
"""       
or1 = Orange(10, 'dark orange')
print(or1.weight)

or1.weight = 100
print(or1.weight)

orange = Orange(200, 'orange')
print(orange.mold)

orange.rot(10, 36)
print(orange.mold)
"""

class Rectangle: #「矩形」
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(4, 5)
print(rectangle.area())

rectangle.change_size(20, 50)
print(rectangle.area())

#チャレンジは7.pyに