# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:21:10 2019
独学プログラマー第1部

@author: ell_Sub2
"""

#for i in range(100):
print("hello, World") 
print("""これは
      ふくすうぎょう
      に渡る""")

#None -> NoneType型
nontype = None

print(5//2) #これは切り捨て

#if 100 = 10: ちゃんとエラーがでるぜェ
#    print("a")

#論理演算はand or notでかける
1 == 1 and 2 == 2 #True
not 1 == 1 #False(真偽値の反転)

#if-else
hoge = 10
if hoge == 9:
    print("hogehoge")
elif hoge == 10:
    print("piyo")
else:
    print("は?")
    
#慣習:変数名と関数名には大文字を使わず、アンダースコアを使う。
def f(x):
    return x*2
    #returnが無ければNoneを返す

print( f(40) )
str(10) #int -> str
int("1") #rev

#標準入力
def old_young():
    age = input("Enter your age:")
    int_age = int(age) #今回の肝
    if int_age <= 19:
        print("you are young!")
    else:
        print("you are old...")
    
#オプション引数
def f(x=2):
    return x*x

print(f()) #2*2
print(f(5)) #5*5

x = 100
def xx():
    global x #グローバル変数にアクセスする場合、そのスコープ内の先頭に宣言する
    x += 1
    print(x)

xx()

#p63例外処理
def division():
    try:
        a = int(input("a / b\n  a:"))
        b = int(input("  b:"))
        print(a/b)
    except (ValueError, ZeroDivisionError): #複数の例外を処理するためには、()を使う
        #print(b) #try節で定義された変数は使用できない。理由は、変数定義よりも前に例外が発生する可能性があるため。
        print("invalid input.")
    
division()

#docstringはこう書く!
def add(x, y):
    """
    Returns x + y. #関数の簡単な説明
    :param x: int. #以降は引数、型、および関数が返す値について書く
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y

#p69 チャレンジ
def sqared(x):
    """
    二乗して返します。
    :param x: int.
    :return: int square x.
    """
    return x**2

def first_func(x):
    return int(x/2)

def second_func(x):
    return x*4

i = first_func(5)
print(i)
print(second_func(i))

def str_to_float(s):
    try:
        return float(s)
    except(NameError, ValueError):
        print ("invalid input")
        
print(str_to_float("3.444"))

#4章ここまで