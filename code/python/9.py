# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:37:54 2019
独学プログラマー 14章
@author: ell_Sub2
"""
"""
class変数
    Pythonでは、classはtypeクラスのインスタンスである。
    ので、classの中身で、普通の変数と同様の(selfを使わず)定義した変数は、
    そのクラスから作られた、どのインスタンスからもアクセスすることが可能である。
    この変数をclass変数と呼ぶ。
    逆に、self.~の変数はインスタンス変数であり、classからインスタンス化されたオブジェクトが、
    個々に保持する値である。
"""
class MotorMaker:
    country = "" #これはクラス変数?
    bikes = []
    def __init__(self, name, c):
        self.name = name #これはインスタンス変数
        self.country = c #もしかして、ここでインスタンス変数になってしまってる?
                         #たぶんそのとおり。strはイミュータブルだから、クラス変数の
                         #countryは書き換わらない...のでは?
                         #イミュータブル:その一部を、入れ替えたり消したりすることができない
    
    def change_country(self, c):
        self.country = c
    
    def print_country(self):
        print("{} is form {}".format(self.name, self.country))
        
    def make_a_bike(self, name):
        self.bikes.append(name)

yamaha = MotorMaker("Yamaha", "Japan")
honda = MotorMaker("Honda", "Japan")

yamaha.change_country("USA") #クラス変数を書き換えたらばhondaさんとこのcountryも変わるはずじゃ...?
yamaha.print_country()
honda.print_country()

yamaha.make_a_bike("Vino")
print(honda.bikes) #Vinoたん...!ホンダに身を売ったのか!!・・・てな感じ。



class Lion: #すべてのクラスはobjectクラスを継承している
    def __init__(self, name):
        self.name = name
    
    def __repr__(self): #特殊メソッド。オブジェクト自体の戻り値を指す
        return self.name #オーバーライドして、self.nameを返すようにしてみる
                         #似たような特殊メソッドに__str__がある

dil = Lion("Dilvert")
print(dil) #self.nameが表示される。



class AlwaysPositive:
    def __init__(self,num):
        self.num = num
    
    def __add__(self, other):
        return abs(self.num + other.num) #otherはintクラス?なぜother.nが可能?
                                         #nってなんか特殊なのかと思ってnumにしたが変化ナシ
x = AlwaysPositive(10)
y = AlwaysPositive(-3)

print(x + y) #__add__があれば"+"演算子が使える...!

"""
Pythonでは、+演算子の左のオブジェクトの__add__メソッドを実行する。
このとき、右側のオブジェクトを__add__メソッドに(勝手に)渡す。
でも、なぜother.nが可能なのか分からない。otherはnというインスタンス変数を持っているのだろうか。
"""


#「is」 is...前後のオブジェクトが同一のオブジェクトならTrue
print(1 is 1) #T
print(1 is not 1.0) #T



#14章チャレンジ
class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []
    def __init__(self, l):
        self.side_len = l
        self.square_list.append(self) ##イケてると思ふ。

    def __repr__(self):
        return (( "{} by ".format(self.side_len) ) * 4)[0:-4] #闇を感じるが動く

s = Square(5)
print(s)

def izu(p1, p2):
    return p1 is p2

print(izu(1, 1.0))

#14章ここまで