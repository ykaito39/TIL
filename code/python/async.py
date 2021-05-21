# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 07:41:21 2019

@author: user
"""

import asyncio

#並列で実行される関数
async def factorial(name, number):
    print("Task %s: Compute facrotial(%s)" % (name, number))
"""
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute facrotial(%s)" % (name, i))
        #await asyncio.sleep(1) #なくても実行できるっぽい
        f *= i
        
    print("Task %s: factorial(%s) = %s" % (name, number, f))
"""
    
#並行して実行したい関数のListを作ってみた
fun = [ factorial(chr(ord("A")+i), i+2) for i in range(5)] 

#イベントループの取得
loop = asyncio.get_event_loop()

#並行して実行したい関数を引数に渡す
result = loop.run_until_complete(asyncio.gather(*fun)) 