//無名関数
var hello = function (name){
	console.log("hello " + name);
}

hello("Tom");
hello("Bob");
//hello(prompt("お名前...","名無しさん"));
 
//即時関数
(function(name) {
	console.log("hello " + name);
})("Katz");
