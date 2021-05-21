# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:37:15 2019

@author: ell_Sub2
"""
import re

txt = None
with open("abst.txt", "r") as f:
   txt = f.read()
   txt = txt.replace(".", ".\n")

with open("abst.txt", "w") as f:
    f.write(txt)