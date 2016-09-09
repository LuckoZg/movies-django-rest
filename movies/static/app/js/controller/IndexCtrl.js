app.controller('IndexCtrl', ['$scope', 'Movie', function($scope, Movie){
	console.log("IndexCtrl");

	$scope.active.page = "index";

	Movie.getTop(function(docs){
		$scope.movies = docs;
	});

}]);