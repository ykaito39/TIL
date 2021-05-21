# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:22:44 2019
独学プログラマー 12章 チャレンジ
@author: ell_Sub2
"""
import math

class Apple:
    def __init__(self, c, s, w, sw):
        self.color = c
        self.size = s
        self.weight = w
        self.sweetness = sw

class Circles:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return (self.radius)**2 * math.pi
    
class Hexagon:
    def __init__(self, l):
        self.side_len = l
    
    def calculate_perimeter(self):
        return self.side_len * 6
    
c= Circles(20)
print(c.area())

h = Hexagon(1)
print(h.calculate_perimeter())

#12章チャレンジここまで