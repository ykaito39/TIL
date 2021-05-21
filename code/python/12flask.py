# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:09:04 2019

@author: ell_Sub2
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world"

app.run(port=8000)