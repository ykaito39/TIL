# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:06:31 2019

@author: user
Node2の実装で挫折
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.left.right = Node(3)
tree.root.right = Node(4)

"""
       root(1)
     2      4
    3
"""


# リストによる多分木を造ってみる
class Node2():
    __depth__ = 0 #現在のツリーの高さ。depthの計算につかう
    def __init__(self, obj):
        pass
    
    #Node2インスタンス(ノード)に新しい子ノードを追加する。
    #複数回実行することで、エッジがたくさんのノードになって多分木になる
    def append(self, node):
        pass
        
        
class Tree():
    def __init__(self, root):
        self.root = Node2(root)
    
    def Depth(self):
        pass

class Om():
    def __init__(self, name):
        self.name = name
        
        
om = Om("19 Accord OM")
tr = Tree(om)

tr.root.append(Node2())



tr.root.edge.append(Node2(2))
print(tr.root.edge[0].depth)

tr.root.edge.append(Node2(3))
print(tr.root.edge[1].depth)

print(tr.root.edge[0].__appended_flag__)
tr.root.edge[0].append(Node2(4)) #ここでappend_flagがTrueにセットされてdepthがインクリされるはず
#print(tr.root.edge[0].edge[0].depth)
#print(tr.root.edge[0].__appended_flag__)

#print(tr.root.edge)