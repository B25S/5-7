var xmlhttp = window.XMLHttpRequest();

//onreadystatechangeΪһ��δ���õĻص���������XMLHttpRequest.open()�������ʱ�����
xmlhttp.onreadystatechange=function(){
	if(xmlhttp.readyState==4 && xmlhttp.status==200){
		//����Ŀ¼����
	}
}

xmlhttp.open("get","content.txt",true);
xmlhttp.send();