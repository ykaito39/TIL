# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:21:06 2019
独学プログラマー 第21章 チケット行列
@author: ell_Sub2
"""
import time
import random

class Queue:
    def __init__(self):
        self.qs = []
    
    """
    独学プログラマーの実装では、
        insert(0, data)でenqueue
        pop()でdequeueしている
    なんか一番最初に入ったのが一番インデックスが大きくなるのがキモかったから変えた
    """
    def enqueue(self, data):
        self.qs.append(data)
    
    def dequeue(self):
        return self.qs.pop(0)
    
    def is_empty(self):
        return self.qs == []
    
    def size(self):
        return len(self.qs)
      
def simulate_line(till_show, max_time):
    """
    :param till_show:整数、上映までの残り時間
    :param max_time: 整数、購入時に要する最大時間(randで使用)
    """
    
    #チケットを買いに来た人何人かをqueueで表現する
    buyers = Queue()
    for i in range(53):
        buyers.enqueue("buyer{}".format(i))
    
    #前処理
    screen_start_time = time.time() + till_show #上映開始時間
    enterd_person = [] #映画館に入れた人
    
    #ループ。映画が始まるか、又は100人全員がチケットを買うまで
    while time.time() <= screen_start_time and not buyers.is_empty():
        time.sleep(random.randint(0, max_time))
        buyer = buyers.dequeue()
        print(buyer)
        enterd_person.append(buyer)
    
    print("---- Oops! 上映開始!! ----")
    
simulate_line(40, 5)