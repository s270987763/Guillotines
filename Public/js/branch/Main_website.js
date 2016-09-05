function webshellList(){
	console.log(1)
	$.ajax({
		url: '/RootApi/webshell/list/1',
		type: 'get',
		dataType: 'text',
		async:false
	})
	.done(function(data){
		console.log(data)
		if(data.type == "success"){
			for(var i = 0;i < data.info.length;i++){
				$(".table tbody").append('<tr><th>' + json.info[i].id + '</th><td>' + Base64.encode(json.info[i].url) + '</td><td>' + json.info[i].category + '</td><td>' + json.info[i].time + '</td><td class="click-dropdown"><div class="btn-group"><button class="glyphicon glyphicon-th-list" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button><ul class="dropdown-menu pull-right"><li><a><span class="glyphicon glyphicon-edit"></span>编辑</a></li><li><a><span class="glyphicon glyphicon-eye-open"></span>浏览</a></li><li><a><span class="glyphicon glyphicon-trash"></span>删除</a></li></ul></div></td>');
			}
		}
	})
}
function addWebShell(){
	$(".col-xs-9 .btn-group button:first").click(function(){
		swal({
			title: "添加WebShell",
			text: '<input type="text" class="form-control alert-input" placeholder="URL"><input type="text" class="form-control alert-input" placeholder="PassWord"><button id="scriptCategory" onClick="fun_scriptCategory()">脚本类型</button><ul class="dom-hidden"><li onClick="reviseButtonText(this)">PHP</li><li onClick="reviseButtonText(this)">ASP</li><li onClick="reviseButtonText(this)">JSP</li><li onClick="reviseButtonText(this)">ASPX</li></ul>',
			html: true,
			showCancelButton: true,
			closeOnConfirm: false,
			confirmButtonText:"添加",
			cancelButtonText:"取消",
		},
		function(){
			var url = $(".alert-input:first").val();
	    	var password = $(".alert-input:eq(1)").val();
	    	var scriptCategory = $(".sweet-alert #scriptCategory").text();
			if(url === "") {
				swal.showInputError("WebShell地址为空！");
				$(".alert-input:first").focus();
				return false;
			}
			if(password === ""){
				swal.showInputError("PassWord为空！");
				$(".alert-input:eq(1)").focus();
				return false;
			}
			if(scriptCategory === "脚本类型"){
				swal.showInputError("脚本类型为空！");
				return false;
			}
			$.ajax({
				url: '/RootApi/webshell/add',
				type: 'post',
				dataType: 'json',
				data:{
					url:url,
					password:password,
					category:scriptCategory
				},
				async:false
			})
			.done(function(data){
				if(data.type == "success"){
					swal({
					    title: "添加成功",
					    text: url + '<br/>' + password,
					    type: 'success',
					    html:true,
					    showCancelButton: false,
					    confirmButtonText:"确定",
					},function(){
						$(".table tbody tr").remove();
						webshellList();
					});
				}else{
					swal({
						title: "添加失败",
						text: data.info,
						type: 'error',
						html:true,
						showCancelButton: false,
						confirmButtonText:"确定",
					});
				}
			})
		});
		$(".sweet-alert p input:eq(0)").blur(function(){
			var scriptFile,fileType,webshellFile;
			if($(this).val() == ""){
				return false;
			}
			scriptFile = ['php','asp','aspx','jsp'];
			webshellFile = parseURL($(this).val()).file.split(".").pop();
			if(webshellFile.indexOf("?") != "-1"){
				webshellFile = webshellFile.split("?")[0];
			}
			scriptFile.forEach(function(index, item){
				if(index == webshellFile.toLowerCase()){
					fileType = index;
				}
			})
			if(fileType){
				$("#scriptCategory").text(fileType);
			}else{
				$("#scriptCategory").text("脚本类型");
			}
		});
	})
}
function reviseButtonText(dom){
	$(dom).parent("ul").prev().text($(dom).text());
	fun_scriptCategory()
}
function fun_scriptCategory(){
	var ul = $(".sweet-alert ul:first");
	if(ul.attr("class") == "dom-hidden"){
		ul.attr('class', 'dom-show');
	}else{
		ul.attr('class', 'dom-hidden');
	}
}
webshellList();
addWebShell();
