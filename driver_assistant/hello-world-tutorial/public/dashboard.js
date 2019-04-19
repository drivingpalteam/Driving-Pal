(function($){

	setInterval(function() {
		$.get("objects.txt", function(response) {
     		var objects = response.split("\n");
     		jQuery("#main span").remove();
     		var people = [];
     		var cars = [];
     		var bikes = [];
     		if (objects[0] != '') {
     			var people = objects[0].split(' ').map(Number);
     		}
     		if (objects[2] != '') {
     			var cars = objects[2].split(' ').map(Number);
     		}
     		if (objects[1] != '') {
     			var bikes = objects[1].split(' ').map(Number);
     		}
     		for (var x = 0; x < people.length; x++) {
     			$("#main").append("<span class='stuck' style='left:" + people[x] * 100 + "%'><img src='images/person.png'/></span>");
     		}
     		for (var x = 0; x < cars.length; x++) {
     			$("#main").append("<span class='stuck car' style='left:" + cars[x] * 100 + "%'><img src='images/car.png'/></span>");
     		}
     		for (var x = 0; x < bikes.length; x++) {
     			$("#main").append("<span class='stuck' style='left:" + bikes[x] * 100 + "%'><img src='images/bike.png'/></span>");
     		}
     	})
	}, 50);

})(jQuery);