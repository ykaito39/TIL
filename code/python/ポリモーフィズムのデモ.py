# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:25:34 2020

@author: ell
ポリモーフィズムのデモ
"""


class TextReader:
    def __init__(self):
        pass
    
    def Read(self):
        pass
    
class NetworkReader(TextReader):
    def __init__(self):
        pass
    
    def Read(self):
        pass
    
class FileReader(TextReader):
    def __init__(self):
        pass
    
    def Read(self):
        pass
    
def PrintText(a):
    a.Read()
    
b = NetworkReader()
PrintText(b)