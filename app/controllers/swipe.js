'use strict';

angular.module('tinderX.swipe', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('swipe', {
		url: '/swipe',
		templateUrl: 'partials/swipe.html',
		controller: 'SwipeCtrl'
	})
}])

.controller('SwipeCtrl', ['$scope', '$http', '$window', function($scope, $http, $window){

	$scope.errors = {}

	// use left / right arrows to swipe
	$window.onkeydown = function(){
		if (event.keyCode == 37) {
			$scope.swipe('left')
		} else if (event.keyCode == 39) {
			$scope.swipe('right')
		}
	}

	// get the first user
 	$http.get('/fetch')
 	.success(function(data) {
 		$scope.user = data.next
 		$scope.errors.api = false
 	}).error(function(data,status) {
 		$scope.errors.api = data.message
 	})

 	// swipe left / right on $scope.user
	$scope.swipe = function(dir){

		// send a POST request to /swipe
		$http.post('/swipe',{
			profile: $scope.user,
			direction: dir
		}).success(function(data){
			$scope.user = data.next
			$scope.errors.api = false
		}).error(function(data,status){
			$scope.errors.api = data.message
		})
	}
}])