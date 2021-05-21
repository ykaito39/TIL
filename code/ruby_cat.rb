# whileによる実装
# getsはcmd引数で与えられたファイルから1行読み込むメソッド
# cmd引数がなければ標準入力から読み込む。
# stringのインスタンスなので.eachできない

n = 1
while line = gets
	printf "%4d : %s",n ,line
		
	n += 1
end
