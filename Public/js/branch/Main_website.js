function webshellList(){
	$.ajax({
		url: '/RootApi/webshell/list',
		type: 'post',
		dataType: 'json',
	})
	.done(function(data){
		if(data.type == "success"){
			for(var i = 0;i < data.info.length;i++){
					$(".table tbody").append('<tr><th>' + json.info[i].id + '</th><td>' + json.info[i].url + '</td><td>' + json.info[i].category + '</td><td>' + json.info[i].time + '</td><td class="click-dropdown"><div class="btn-group"><button class="glyphicon glyphicon-th-list" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button><ul class="dropdown-menu pull-right"><li><a><span class="glyphicon glyphicon-edit"></span>编辑</a></li><li><a><span class="glyphicon glyphicon-eye-open"></span>浏览</a></li><li><a><span class="glyphicon glyphicon-trash"></span>删除</a></li></ul></div></td>');
			}
		}
	})
}
/*
	添加webshell
*/
function addWebShell(){
	$(".col-xs-9 .btn-group button:first").click(function(){
		swal({
			title: "添加WebShell",
			text: '<input type="text" class="form-control alert-input" placeholder="URL"><input type="text" class="form-control alert-input" placeholder="PassWord"><button id="scriptCategory">脚本类型</button>',
			html: true,
			showCancelButton: true,
			closeOnConfirm: false,
			confirmButtonText:"添加",
			cancelButtonText:"取消",
		},
		function(){
			swal.showInputError("PassWord为空！");
		});
	})
}
function addWebShell_bak(){
    $(".col-xs-9 .btn-group button:first").click(function(){
	    swal({
	        title: "添加WebShell",
	        text: '请在下面输入地址与密码<small style="color: darkgray;padding-left: 20px;">类别如不选择，则为“默认”</small><br><input type="text" class="form-control alert-input" placeholder="URL"><input type="text" class="form-control alert-input" placeholder="PassWord"><button class="button-info">脚本类型</button><ul class="dom-hidden"><li onClick="reviseButtonText(this)">php</li><li onClick="reviseButtonText(this)">asp</li><li onClick="reviseButtonText(this)">aspx</li><li onClick="reviseButtonText(this)">jsp</li></ul><button class="button-info">默认</button><ul class="dom-hidden"></ul>',
	        html: true,
	        showCancelButton: true,
	        closeOnConfirm: false,
	        confirmButtonText:"添加",
	        cancelButtonText:"取消",
	    },
	    function(){
	    	var url = $(".alert-input:first").val();
	    	var password = $(".alert-input:eq(1)").val();
	    	var fileType = $(".sweet-alert .button-info:first").text();
	    	var category = $(".sweet-alert .button-info:last").text();
			if (url === "") {
				swal.showInputError("WebShell地址为空！");
				return false;
			}
			if(password === ""){
				swal.showInputError("PassWord为空！");
				$(".alert-input:eq(1)").focus();
				return false;
			}
			if(fileType === "脚本类型"){
				swal.showInputError("脚本类型为空！");
				$(".alert-input:last").focus();
				return false;
			}
			$(".confirm").text("Doing...");
	    	if(url.substr(0, 4) != "http"){
	    		url = "http://" + url;
	    	}
	    	$.ajax({
	    		url: 'data/data_api.php',
	    		type: 'post',
	    		dataType: 'text',
	    		data: "function=url-pass&url=" + Base64.encode(encodeURI(url)) + "&password=" + Base64.encode(password) + "&filetype=" + Base64.encode(fileType)  + "&category=" + Base64.encode(category),
	    		async:false
	    	})
	    	.done(function(data){
	    		console.log(data)
	    		if(data == "200"){
					swal({
					    title: "添加成功",
					    text: $(".alert-input:first").val() + '<br/>' + $(".alert-input:last").val(),
					    type: 'success',
					    html:true,
					    showCancelButton: false,
					    confirmButtonText:"确定",
					},function(){
						$(".table tbody tr").remove();
						webshellList();
					});
	    		}else if(data == "404"){
					swal({
					    title: "添加失败",
					    text: "网站无法连接，请确认后输入<br /><br />" + $(".alert-input:first").val(),
					    type: 'error',
					    html:true,
					    showCancelButton: false,
					    confirmButtonText:"确定",
					});
	    		}else if(data == "502"){
					swal({
					    title: "添加失败",
					    text: "网站密码不正确，请确认后输入<br /><br />" + $(".alert-input:first").val() + '<br/>' + $(".alert-input:last").val(),
					    type: 'error',
					    html:true,
					    showCancelButton: false,
					    confirmButtonText:"确定",
					});
	    		}
	    	})
	    });
		$(".sweet-alert p input:eq(0)").blur(function(){
			var scriptFile = ['php','asp','aspx','jsp'];
			var fileType;
			var webshellUrl = parseURL($(this).val());
			if($(this).val() == ""){
				return false;
			}
			scriptFile.forEach(function(index, item){
				if(index == $(webshellUrl.segments[0]).selector.split(".")[1]){
					fileType = index;
				}
			})
			if(!fileType){
				$(".alert-input:last").val("");
				return false;
			}
			$(".sweet-alert .button-info:first").text(fileType);
		});
		$(".sweet-alert .button-info:first").click(function(){
			if($(".sweet-alert ul:first").attr("class") == "dom-hidden"){
				if($(".sweet-alert ul:first").attr("data") != "yes"){
					$(".sweet-alert ul:first").attr('data', 'yes');
				}
				$(".sweet-alert ul:first").attr('class', 'dom-show');
			}else{
				$(".sweet-alert ul:first").attr('class', 'dom-hidden');
			}
		});
		$(".sweet-alert .button-info:last").click(function(){
			if($(".sweet-alert ul:last").attr("class") == "dom-hidden"){
				if($(".sweet-alert ul:last").attr("data") != "yes"){
					$.post('data/data_api.php', {function: 'category-list'}, function(data){
						$(".sweet-alert ul:last").append(data);
						$(".sweet-alert ul:last").attr('data', 'yes');
					});
				}
				$(".sweet-alert ul:last").attr('class', 'dom-show');
			}else{
				$(".sweet-alert ul:last").attr('class', 'dom-hidden');
			}
		});
	});
}
/*
	点击内容，更换button text
*/
function reviseButtonText(dom){
	$(dom).parent("ul").prev().text($(dom).text())
}
// webshellList();
addWebShell();
// total(".button-info>b");
$("#asd").click(function(){
	return false;
})
