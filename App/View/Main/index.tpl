<<<<<<< HEAD
test
=======
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>血滴子 - Guillotines</title>
    <link rel="stylesheet" href="/Public/css/library/bootstrap/bootstrap.css">
    <link rel="stylesheet" href="/Public/css/branch/Main_index.css">
</head>
<body>
<div class="container">
    <div class="row">
    <include file="Public/html/leftnav.html" />
        <div class="col-xs-9">
            <button class="button-info"><span class="glyphicon glyphicon-flash"></span>WebShell总数：<b>{$total}</b></button>
            <div style="clear:both"></div>
            <div class="hr-text">
                <h6>近7天，每天上传的WebShell数量统计报表</h6>
            </div>
    		<canvas id="Statistics"></canvas>
            <div class="hr-text">
                <h6>站点类别</h6>
            </div>
            <div class="list-group">
            </div>
        </div>
    </div>
</div>
</body>
<script type="text/javascript" src="/Public/js/library/jquery.js"></script>
<script type="text/javascript" src="/Public/js/library/bootstrap.js"></script>
<script type="text/javascript" src="/Public/js/library/Chart.js"></script>
<script type="text/javascript" src="/Public/js/branch/Main_index.js"></script>
<script type="text/javascript">
	var lineChartData = {
		labels :eval({$reportForm})['Labels'],
		datasets : [
			{
				fillColor : "transparent",
				strokeColor : "#1BC98E",
				pointColor : "#1BC98E",
				pointStrokeColor : "#fff",
				data : eval({$reportForm})['Total']
			}
		]
	}
	var myLine = new Chart(document.getElementById("Statistics").getContext("2d")).Line(lineChartData);
</script>
</html>
>>>>>>> origin/master
