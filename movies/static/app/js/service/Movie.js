app.factory('Movie', ['$location', '$route', '$http', function($location, $route, $http){
	
	var Movie = {

		getTop: function(callback){
			$http.get("http://127.0.0.1:8000/api/").success(function(response){
				callback(response);
			}).error(function(err){
				console.log(err);
			});
		},

		getList: function(callback){
			$http.get("http://127.0.0.1:8000/api/list/").success(function(response){
				callback(response);
			}).error(function(err){
				console.log(err);
			});
		},

		getDetail: function(id, callback){
			$http.get("http://127.0.0.1:8000/api/" + id + "/").success(function(response){
				callback(response);
			}).error(function(err){
				console.log(err);
			});
		}

	};
	
	return Movie;

}]);