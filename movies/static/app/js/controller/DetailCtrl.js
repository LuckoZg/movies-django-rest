app.controller('DetailCtrl', ['$scope', '$routeParams', 'Movie', function($scope, $routeParams, Movie){
	console.log("DetailCtrl");

	$scope.active.page = "";

	if($routeParams.id)
		id = $routeParams.id;

	Movie.getDetail(id, function(docs){
		$scope.movie = docs[0];
		console.log(docs[0])
	});

}]);