# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:39:24 2020

@author: ell
"""

#socket用の待ちを発生させるプログラム

import time

def test(t):
    for i in range(t):
        print(i)
        time.sleep(1)
        
if __name__ == "__main__":
    test(50)