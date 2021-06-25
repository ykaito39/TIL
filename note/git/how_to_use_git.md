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

