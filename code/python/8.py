# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:35:47 2019
独学プログラマー 13章
@author: ell_Sub2
"""

"""
オブジェクト指向の重要な4概念
    「カプセル化」「抽象化」「ポリモーフィズム」「継承」
    
カプセル化
    ・オブジェクトに、複数の状態(インスタンス変数)と状態を変更する方法(メソッド)をもたせる
    ・インスタンス変数はクラス外部から参照できない。
抽象化
    ・本質的な特徴だけ集めた状態にすること。
    ・いらない部分、細かい部分は取り除く。
ポリモーフィズム
    ・同じインターフェース(関数/メソッド)でも、データ型によって違った挙動をする機能
継承
    ・遺伝的継承に似ているらしい
"""

########################################
# カプセル化
########################################
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
        
    def change_data(self, index, n):
        self.nums[index] = n

"""
#↑class文の内部と区別して、cliantという言葉を使う。
#↓本書のいう「cliant側」
data1 = Data()
data1.nums[0] = 100 #直接変更。カプセル化の概念上良くない。
print(data1.nums)

data1.change_data(3, 20) #クラスの外からオブジェクトを利用するメソッド=cliant
print(data1.nums)
"""

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe" #「_」から始まるインスタンス変数は、clientから使うべきでない
    
    def public_method(self):
        pass
    
    def _unsafe_method(self): #メソッドも同様
        pass
    

########################################
# ポリモーフィズム
########################################
print("hello, world!")
print(1) #同じprintメソッドでも、引数の型はそれぞれ
print(["YAMAHA", "HONDA", "KTM"]) #でも出力はすべて標準出力

#「ダック・タイピング」=それがアヒルのように鳴き、アヒルのように歩くのなら、それはアヒルだ。


########################################
# 継承
########################################
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape): #継承
    def area(self):
        return self.width * self.len
    
    def print_size(self): #オーバーライド(上書き),ひょっとしてこれでポリモーフィズムしてるんか?
        print("I am {} by {}".format(self.width, self.len))

a_sq = Square(20, 20)
a_sq.print_size()


########################################
# コンポジション:「has-a」関係
########################################
"""
別クラスのオブジェクトをもたせることで、主従関係(持っている、持たれている)を実現できる
"""
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

jack = Person("Jack owel")
poppy = Dog("poppy", "pomeranian", jack)

print(poppy.owner.name) #「.」でつなげるやつってこうやって実装されてたんや...


#よっしゃ13章チャレンジや!
class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calc_perimeter(self):
        return 2*(self.width + self.len)

class Square(Shape):
    def __init__(self, l):
        self.side_len = l
    
    def calc_perimeter(self):
        return 4 * self.side_len
    
    def change_size(self, size):
        self.side_len += size
        if self.side_len <= 0:
            self.side_len = 0

r = Rectangle(10, 2)
s = Square(5)

print(r.calc_perimeter())
print(s.calc_perimeter())

s.change_size(-1)
print(s.calc_perimeter())

r.what_am_i()
s.what_am_i()


class Horse:
    def __init__(self, name, color, owner):
        self.name = name
        self.color = color
        self.owner = owner
    
class Rider:
    def __init__(self, name):
        self.name = name
        
rick = Rider("Rick deen")
gurasuwanda = Horse("Glass Wander", "栗毛", rick)

print(gurasuwanda.owner.name)

#13章終わり