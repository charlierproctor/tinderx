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

	$scope.errors = {}

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