var xmlhttp = window.XMLHttpRequest();

//onreadystatechange为一个未设置的回调函数，在XMLHttpRequest.open()请求完毕时候调用
xmlhttp.onreadystatechange=function(){
	if(xmlhttp.readyState==4 && xmlhttp.status==200){
		//设置目录布局
	}
}

xmlhttp.open("get","content.txt",true);
xmlhttp.send();