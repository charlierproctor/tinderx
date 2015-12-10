'use strict';

angular.module('tinderX.swipe', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('swipe', {
		url: '/swipe',
		templateUrl: 'partials/swipe.html',
		controller: 'SwipeCtrl'
	})
}])

.controller('SwipeCtrl', ['$scope', '$http', function($scope, $http){

 	$http.get('/fetch')
 	.success(function(data) {
 		$scope.user = data
 	}).error(function(data,status) {
 		// TODO: handle the error
 	})

	$scope.left = function(){
		$http.post('/swipe',{
			user: user,
			direction: 'left'
		})
	}

	$scope.right = function(){
		$http.post('/swipe',{
			user: user,
			direction: 'right'
		})
	}
}])