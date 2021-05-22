// console.dir(window);
// console.log(window.outerHeight);	//windowの高さ
// window.location.href = "http://google.com";	//hrefを書き換える


//DOM = document object model
//window.document - 今開いているページ(windowは省略可能)

var e = document.getElementById('msg');	//idを取得.今回はindex.html内のmsgにアクセスしている
e.textContent = 'hello!';	//書き換え
e.style.color = 'red';		//スタイルの追加
e.className = 'myStyle';	//スタイル・クラスを指定

//add idに対してイベントを紐付ける.
//addEventListener(どのような場合に,ナニをする(関数));
document.getElementById('add').addEventListener('click', function() {
	var greet = document.createElement('p'),
	text = document.createTextNode('hello, world');
	document.body.appendChild(greet).appendChild(text);	//body内にgreet(<p>)を配置,更に中身に'hello, world'を入れる.
});
