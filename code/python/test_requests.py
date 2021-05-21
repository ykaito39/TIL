# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:05:06 2019

@author: ell_Sub2
"""


import requests
import urllib.request

site = "https://news.google.jp"


r1 = requests.get(site)
html1 = r1.text

