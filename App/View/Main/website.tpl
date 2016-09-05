﻿<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>受控站点 - Guillotines</title>
    <link rel="stylesheet" href="/Public/css/library/bootstrap/bootstrap.css">
    <link rel="stylesheet" href="/Public/css/library/sweetalert.css">
	<link rel="stylesheet" href="/Public/css/branch/base.css">
    <link rel="stylesheet" href="/Public/css/branch/Main_website.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-xs-3">
		    <ul class="nav nav-tabs nav-stacked" data-spy="affix">
		    	<span>Guillotines</span>
		    	<form class="nav-tabs-form">
		      		<input class="form-control" type="text" placeholder="Search...">
		      		<button type="submit">
		        		<span class="glyphicon glyphicon-search"></span>
		      		</button>
		    	</form>
		    	<li class="nav-list-span">功能列表</li>
		        <li><a href="/Main/index">首页</a></li>
		        <li><a href="/Main/website">受控站点</a></li>
		        <li><a href="/Main/updata">更新站点</a></li>
		        <li><a href="/Main/operation">统一操作</a></li>
		        <li><a href="/Main/database">数据库操作</a></li>
		    </ul>
		</div>
        <div class="col-xs-9">
            <div class="btn-group" role="group">
                <button type="button" class="btn btn-default">添加WebShell</button>
                <button type="button" class="btn btn-default">批量添加</button>
                <button type="button" class="btn btn-default">批量删除</button>
            </div>
            <div class="btn-group" role="group">
                <button type="button" class="btn btn-default">上一页</button>
                <button type="button" class="btn btn-default">下一页</button>
            </div>
            <button class="button-info"><span class="glyphicon glyphicon-flash"></span>WebShell总数：<b>{{total_webshell}}</b></button>
            <button class="button-info button-info-refresh"><span class="glyphicon glyphicon-refresh"></span></button>
            <table class="table">
                <thead>
                    <tr>
                        <th>序列</th>
                        <th>地址</th>
                        <th>类别</th>
                        <th>时间</th>
                        <th>功能</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>
    </div>
</div>
</body>
<script type="text/javascript" src="/Public/js/library/jquery.js"></script>
<script type="text/javascript" src="/Public/js/library/bootstrap.js"></script>
<script type="text/javascript" src="/Public/js/library/sweetalert.js"></script>
<script type="text/javascript" src="/Public/js/branch/base.js"></script>
<script type="text/javascript" src="/Public/js/branch/Main_website.js"></script>
</html>
