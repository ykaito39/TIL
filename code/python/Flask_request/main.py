# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:55:16 2020

@author: ell
"""

import os
from flask import Flask, request, Markup, abort, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    html = '''
    <form action="/test" enctype="multipart/form-data"> <!--multi...を設定しないとPOSTされない-->
        <p><label>test: </label>
        <input type="file" name="query" value="default">
        <button type="submit" formmethod="POST">POST</button></p>
    </form>
    '''
    
    return Markup(html)

@app.route("/test", methods=["GET", "POST"])
def test():
    try:
        if request.method == "GET":
            return request.args.get("query", "")
        elif request.method == "POST":
            if "query" not in request.files: #queryが存在しないっぽい
                #flash("ファイルがありません")
                print("しっぱい")
                return redirect(request.url)
                
            #return request.form["query"]
            file = request.files["query"] #inputのnameを入れる
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            return redirect(url_for("uploaded_file", filename=filename)) #uploaded_fileの関数に飛ばす,第に2以降が引数になる
        else:
            return abort(400)
        
    except Exception as e:
        return str(e)
    

@app.route("/uploaded/<filename>") #<引数名>で与えること!!!
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    
    
if __name__ == "__main__":
    app.run()