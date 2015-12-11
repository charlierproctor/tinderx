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
 		$scope.user = data.next
 	}).error(function(data,status) {
 		// TODO: handle the error
 	})

	$scope.left = function(){
		$http.post('/swipe',{
			user: $scope.user,
			direction: 'left'
		}).success(function(data){
			$scope.user = data.next
		}).error(function(data,status){

		})
	}

	$scope.right = function(){
		$http.post('/swipe',{
			user: $scope.user,
			direction: 'right'
		}).success(function(data){
			$scope.user = data.next
		}).error(function(data,status){

		})
	}
}])