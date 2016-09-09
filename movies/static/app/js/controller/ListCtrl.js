app.controller('ListCtrl', ['$scope', 'Movie', function($scope, Movie){
	console.log("ListCtrl");

	$scope.active.page = "list";

	Movie.getList(function(docs){
		$scope.movies = docs;
	});

}]);