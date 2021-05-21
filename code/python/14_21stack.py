# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:21:06 2019
独学プログラマー 第21章 Stack
@author: ell_Sub2
"""

"""Stack
Last In First Out
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
        
    def pop(self):
        return self.items.pop()
    
    def push(self, data):
        self.items.append(data)
    
    def peek(self): #スタックの一番上の要素を返すが、消さない(popしないが、参照はできる)
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stk = Stack()

for s in "あんぱんまん":
    stk.push(s)

reversed_str = ""
while not stk.is_empty(): #本書ではwhile stack.sie():してる
    s = stk.pop()
    reversed_str += s

print(reversed_str)