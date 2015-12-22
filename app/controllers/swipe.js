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

	// not waiting for any requests
	$scope.waiting = false

	// update the display with a new profile
	var updateProfile = function(data){
		$scope.waiting = false
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
		$scope.waiting = false
		$scope.errors.api = data.message
	}

	// fetch a user
	$scope.fetch = function(){

		if (!$scope.waiting) {
			// start waiting
			$scope.waiting = true

			// send a GET request to /fetch
			$http.get('/fetch')
		 	.success(updateProfile)
		 	.error(handleError)
		}
	}

	// fetch the first user
	$scope.fetch()

 	// swipe left / right on $scope.user
	$scope.swipe = function(dir){

		if ($scope.waiting) {
			// don't do anything... we're waiting for a prior response
		
		} else if ($scope.errors.noValidFaces) {
			// don't swipe if there aren't any valid faces
			$scope.fetch()

		} else {
			// start waiting
			$scope.waiting = true

			// send a POST request to /swipe
			$http.post('/swipe',{
				profile: $scope.user,
				direction: dir,
				prediction: ($scope.user && $scope.user.prediction) || false
			})
			.success(updateProfile)
			.error(handleError)
		}
	}
}])