/*組み込みオブジェクト:
	- String
	- Array
	- Math
	- Date

*/

var s = new String("yoshida");
console.log(s.length);				//文字数
console.log(s.replace("y", "Y"));	//置換
console.log(s.substr(1, 3));		//1インデックス目から3文字分


var a = new Array(100, 300, 500);
console.log(a.length);				//要素数
// unshift -> array <- push
// shift   <- array -> pop
a.push(700);
console.log(a);

a.splice(1, 2, 800, 900);	//1インデックス目から2個要素を消す. そこから800,900を追加する = [100, 800, 900, 700]
console.log(a);


console.log(Math.PI);
console.log(Math.ceil(5.3));	//切り上げ,6
console.log(Math.floor(5.3));	//切り捨て,5
console.log(Math.round(5.3));	//四捨五入,5
console.log(Math.random());		//0から1未満の数字を返す


var d = new Date();	//現在の時間
//var c = new Date(2014, 1, 11, 10, 20, 30);	//月のみ0から始まる.今回の場合は1なので,2月ということである.
console.log(d.getFullYear());	//2015
console.log(d.getMonth());		//2(0から数える)
console.log(d.getTime());		//1970/1/1からの経過ミリ秒
