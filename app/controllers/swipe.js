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

 	$http.get('/fetch')
 	.success(function(data) {
 		$scope.user = data.next
 		$scope.errors.api = false
 	}).error(function(data,status) {
 		$scope.errors.api = data.message
 	})

	$scope.left = function(){
		$http.post('/swipe',{
			user: $scope.user,
			direction: 'left'
		}).success(function(data){
			$scope.user = data.next
			$scope.errors.api = false
		}).error(function(data,status){
			$scope.errors.api = data.message
		})
	}

	$scope.right = function(){
		$http.post('/swipe',{
			user: $scope.user,
			direction: 'right'
		}).success(function(data){
			$scope.user = data.next
			$scope.errors.api = false
		}).error(function(data,status){
			$scope.errors.api = data.message
		})
	}
}])