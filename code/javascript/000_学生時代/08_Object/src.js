//object: 名前と値がグループ化サれたデータ
/*
var usr = {
	email: "yoshida@gmail.com",	//プロパティ
	score: 80
};

console.log(usr["email"]);	//yoshida@g....
console.log(usr.email);		//yoshida@g....

usr.score = 10;
console.log(usr.score);//10
console.log(usr);
*/

//メソッド:	関数のプロパティ
var usr = {
	email: "yoshida@gmail.com",	//プロパティ
	score: 80,
	greet: function(name){		//メソッド
		console.log("hello, " + name + " from " + this.email + ".");//this: メソッドが属するオブジェクト
	}
};

usr.greet("Tom");
