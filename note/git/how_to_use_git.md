# gitの基礎
## コマンドの意味
|コマンド|意味|
|--|--|
|clone|gitレポジトリの内容をローカルへダウンロードする|
|pull|現在checkoutされているローカルリポジトリと接続されたリモートリポジトリの更新内容を、ローカルリポジトリに反映する。このとき、競合があるとマージを催促される、、、はず。|
|push|commitされた更新をリモートリポジトリへpushする。|
|mearge|現在のリポジトリに対して差分があるリポジトリの情報をマージする。万が一同じ場所を編集している場合は手動で編集が必要となる。|
|checkout|今いるブランチを切り替える。|
  
## ブランチについて
ブランチには大きく分けてリモートとローカルがある。  
gitの標準では、リモートリポジトリは`origin`という名称の配下で示す。  
`origin`上にあるブランチ名は、ローカルのブランチ名と一致していることが推奨される(多分ブランチ作成時、どのリモートリポジトリに接続するかは選択できる気がする...)。  



# 共有ディレクトリでgitを使う場合
## 複数人で使う場合
複数人でgitを使用する場合はgitサーバーが必要が、sambaやネットワークドライブとしてマウントされたものを使用することができる。  
コマンドはこちら。  
  
```sh
$ cd W://repository
$ git init --bare --shared
```
  
こうして作成したgitレポジトリに対して、ローカル(WindowsならCドライブ以下など)にcloneすることで、gitとして管理可能。  
また、gitの設定で編集者情報を入力しておけば誰が変更したかを追っかけることも可能。  

## 個人で使う場合
個人で複数端末を使ってgit管理する場合は、クラウドのファイルサーバーを使用すると良い。例えばGoogle driveやOne driveがこれに当たる。  
Windows上にマウントすることが可能なしくみを使うと、ログイン時に最新のデータが反映される。  



# gitの変更履歴を取り消すには  
git addしたものを取り消すには、git reset HEADで取り消せる。  
  
# githubに接続するまでの一番最初の設定 
## sshの設定  
chmod 755 ~/.ssh  
ssh-keygen -t rsa -f id_rsa_github  
ssh -T git@github.com  
  
## Gitの初期設定
git config --global user.name USERNAME  
git config --global user.email USEREMAIL  
  
## レポジトリごとの設定  
cd my-repository-dir  
git init  
git remote add origin https://github/USERNAME/REPOSITORY-NAME.git  
git push -u origin main  

