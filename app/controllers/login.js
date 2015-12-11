'use strict';

angular.module('tinderX.login', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('login', {
		url: '/',
		templateUrl: 'partials/login.html',
		controller: 'LoginCtrl'
	})
}])

.controller('LoginCtrl', ['$scope', 'Facebook', '$http', '$cookies', '$state',
	function($scope, fb, $http, $cookies, $state){
		$scope.errors = {}

		$scope.login = function() {

			fb.login(function(res) {
				if (res.status == "connected") {
					
					$scope.errors.facebook = false

					var user = {
						fbid: res.authResponse.userID,
						fbAccessToken: res.authResponse.accessToken
					}

					$http.post('/login',user)
					.success(function(data){

						$scope.errors.api = false

						$cookies.put('fbid',user['fbid'])
						$cookies.put('fbAccessToken',user['fbAccessToken'])

						$state.go('swipe')

					}).error(function(data,status){
						$scope.errors.api = data.message
					})
				} else {
					$scope.errors.facebook = res.status
				}
			})

		}
}])