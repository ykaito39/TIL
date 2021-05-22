//setInterval(処理,ミリ秒);	ミリ秒ごとに処理を行う
//setTimeout(処理,ミリ秒);	ミリ秒後に処理を行う(1度のみ)

var i = 0;
function show(){
	console.log(i++);
	var tid = setTimeout(function(){
		show();
	}, 1000);
	if(i > 3){
		clearTimeout(tid);
	}
}
show();

