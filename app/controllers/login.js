'use strict';

angular.module('tinderX.login', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('login', {
		url: '/',
		templateUrl: 'partials/login.html',
		controller: 'LoginCtrl'
	})
}])

.controller('LoginCtrl', ['$scope', 'Facebook', '$http', '$cookies',
	function($scope, fb, $http, $cookies){
		$scope.login = function() {

			fb.login(function(res) {
				if (res.status == "connected") {

					var user = {
						fbid: res.authResponse.userID,
						fbAccessToken: res.authResponse.accessToken
					}
					console.log(user)

					$http.post('/login',user)
					.success(function(data){
						console.log(data)

						// TODO: only login when successful
						$cookies.put('fbid',user['fbid'])
						$cookies.put('fbAccessToken',user['fbAccessToken'])

					}).error(function(data,status){
						// TODO: do something on error. AND on facebook login error
					})
				}
			})
		}
}])