# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:21:06 2019
独学プログラマー 第21章 queue
@author: ell_Sub2
"""

"""queue
First In First Out
"""

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
      
q = Queue()

for i in range(0, 5):
    q.enqueue(i)
    
while not q.is_empty():
    print(q.dequeue())