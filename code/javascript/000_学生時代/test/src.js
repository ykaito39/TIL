var DelStr = function(str){
	while(document.body.innerHTML.indexOf(str,0) != -1){ 
		document.body.innerHTML = document.body.innerHTML.replace(str, "パ");
	}
}

DelStr('す');
