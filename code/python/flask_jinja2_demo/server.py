# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:37:22 2020

@author: ell
"""


from flask import Flask, render_template, request
import os
import random, string

app = Flask(__name__)

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

DB = [(i, "{}".format(randomname(i))) for i in range(1, 100)] #擬似的なDB
print(DB)

@app.route("/index")
def index():
    if request.method == "GET":
        page = request.args.get("page") #/indexにアクセスすると変な値が取得されるためtryする
        
        try:
            if page != "" and page != None:
                page = int(page)
            else:
                page = 1
        except:
            page = 1
        
        print(page)
        if int(page) <= 1 or page == None:
            #25個だけDBから取得してrender_templateする
            #if GETでpage=2になったら、次のページを取得
            links =["", "/index?page=2"]
            return render_template("index.html", file_lis = DB[:25], links=links)
        else:
            links =["/index?page={}".format(page-1), "/index?page={}".format(page+1)]
            DB_tmp = DB[25*(page-1):25*page] #DBから25県取得
            return render_template("index.html", file_lis = DB_tmp, links=links)
    
    return "test"

if __name__ == "__main__":
    app.run(port=8001, debug=False)