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
	$scope.swipeable = false

	// fetch the first user
	$scope.fetch()

	// use left / right arrows to swipe
	$window.onkeydown = function(){
		if (event.keyCode == 37) {
			$scope.swipe('left')
		} else if (event.keyCode == 39) {
			$scope.swipe('right')
		}
	}

	// update the display with a new profile
	var updateProfile = function(data){
		$scope.user = data.next
		$scope.errors.api = false

		// can we swipe on this user?
		$scope.swipeable = !($scope.user.error && ($scope.user.error.type == "NoValidFaces"))

		// have we made a prediction? (maybe no liked_img or disliked_img)
		$scope.prediction = $scope.user.prediction || false
	}

	// handle an api error
	var handleError = function(data,status){
		$scope.errors.api = data.message
	}

	// fetch a user
	$scope.fetch = function(){

		// send a GET request to /fetch
		$http.get('/fetch')
	 	.success(updateProfile)
	 	.error(handleError)
	}

 	// swipe left / right on $scope.user
	$scope.swipe = function(dir){

		// send a POST request to /swipe
		$http.post('/swipe',{
			profile: $scope.user,
			direction: dir
		})
		.success(updateProfile)
		.error(handleError)
	}
}])