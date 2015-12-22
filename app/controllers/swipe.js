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

	$scope.errors = {
		api: false,
		noValidFaces: false,
		noImageYet: false
	}

	// use left / right arrows to swipe
	$window.onkeydown = function(){
		if (event.keyCode == 37) {
			$scope.swipe('left')
		} else if (event.keyCode == 39) {
			$scope.swipe('right')
		}
	}

	// changes to $scope.random force angular to reload the image
	$scope.random = 0

	// update the display with a new profile
	var updateProfile = function(data){
		$scope.random = Math.floor((Math.random() * 1000))
		$scope.user = data.next
		$scope.stats = data.stats

		// calculate the errors
		$scope.errors.api = false
		$scope.errors.noValidFaces = ($scope.user.error 
			&& ($scope.user.error.type == "NoValidFaces"))
		$scope.errors.noImageYet = ($scope.user.error
			&& ($scope.user.error.type == "NoImageYet"))

		// send the image name through
		if ($scope.errors.noImageYet) {
			$scope.errors.noImageYet = $scope.user.error.img_name
		}
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

	// fetch the first user
	$scope.fetch()

 	// swipe left / right on $scope.user
	$scope.swipe = function(dir){

		// don't swipe if there aren't any valid faces
		if ($scope.errors.noValidFaces) {
			$scope.fetch()

		} else {
			// send a POST request to /swipe
			$http.post('/swipe',{
				profile: $scope.user,
				direction: dir
			})
			.success(updateProfile)
			.error(handleError)
		}
	}
}])