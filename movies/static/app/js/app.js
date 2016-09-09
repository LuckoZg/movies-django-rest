var app = angular.module('app', ['ngRoute']);

app.config(function($routeProvider, $locationProvider){
	$routeProvider
	.when('/', {
		templateUrl: '../static/app/view/home.html'
	})
	.when('/list', {
		templateUrl: '../static/app/view/list.html'
	})
	.when('/:id', {
		templateUrl: '../static/app/view/detail.html'
	})
	.otherwise({
		redirectTo: '/'
	});

	$locationProvider.html5Mode(true);
});