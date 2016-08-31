// 
// /*
// 	站点类别数目统计
// */
// function website_category(){
// 	$.post('/data/data_api.php', {function: 'website-category'},function(data) {
// 		data = data.substring(0,data.length-1).split(",");
// 		data = data.map(function(index) {
// 			index = index.split("$#!");
// 			$(".list-group").append('<button class="list-group-item"><span class="badge">'+ index[1] +'</span>'+ index[0] +'</button>');
// 		})
// 	});
// }
//
// $(document).ready(function($){
// 	website_category();
// });
