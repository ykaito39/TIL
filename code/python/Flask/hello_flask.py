#クイックスタート:https://a2c.bitbucket.io/flask/quickstart.html
from flask import Flask, redirect
import os
import time

print(os.getcwd())

app = Flask(__name__)
#app.config["SERVER_NAME"] = "/sava/"

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello():
    return "hello world"

#URLで値を渡す(非クエリストリング)
@app.route("/user/<username>")
def show_user_profile(username): #<username>の中身を変数名として扱う?
    return "hello {}".format(username) #ユーザー名を与えて、DBから情報を取り出すことが可能?

@app.route("/post/<int:post_id>") #型の指定が可能(int, float, path)
def show_post(postid): #変数名は<>の中身と一致しなくてもいいみたい。
    return str(postid)

#リダイレクト
@app.route("/logout")
def logout():
    print("ログアウトします")
    time.sleep(2)
    return redirect("") #うまく動かない(""で無限ループ)
    


#エラーのハンドリング
#@app.errorhandler(404)
#def no_url():
#    return "そんなURLねえよ"
    
    
    
if __name__ == "__main__":
    app.run(port=8000, debug=False)