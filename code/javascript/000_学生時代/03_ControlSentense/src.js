var value = 20;

if(value == 10){			//false
	console.log('A');
}else if(value < 30){		//true, screen 'B'.
	console.log('B');
}else if(value == 20){		//true, but not screen. 
	console.log('C');
}

//文字列:	空文字以外だったら true
//数値:		0 か NaN 以外だったら true
//true / false
//object:	null 以外だったら true
//undefined, null -> falsea
 
var x = 'ok!';
if(x){//空文字でなければ
	//処理
	console.log(x);
}

//三項演算子
var max, x, y;
max = (x > y) ? x : y;

//switch sentense 
var signal = 'pink';
switch(signal){
	case 'red':
		console.log("stop!");
		break;
	case 'yellow':
		console.log("slow down!");
		break;
	case 'blue':
		console.log("go go!");
		break;
	default:
		console.log("wrong signal");
		break;
}

//loop
var i = 0;
while(i < 10){
	console.log(i);
	i++;
}

do {
	console.log(i);
	i++;
}while(i < 10);

//break: loopを抜ける
//continue: loop処理を一回飛ばす
for(var i = 0; i < 10; i++){
	if(i == 5){
		//break;
		continue;
	}
	console.log(i);
}
