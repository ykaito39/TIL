# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:11:05 2019
独学プログラマー 8章で作るモジュールのファイル
@author: ell_Sub2
"""

def print_hello():
    print('hello')
    
#これはテスト用等に使う。
#インポート先ではhello!は出力されないが、ここでは出力される。
if __name__ == "__main__":
    print('hello!')