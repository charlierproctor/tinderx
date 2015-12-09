'use strict';

angular.module('tinderX.login', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('login', {
		url: '/',
		templateUrl: 'partials/login.html',
		controller: 'LoginCtrl'
	})
}])

.controller('LoginCtrl', ['$scope', 'Facebook', '$http', 
	function($scope, fb, $http){
		$scope.login = function() {
			fb.login(function(res) {
				if (res.status == "connected") {

					var user = {
						fbid: res.authResponse.userID
					}

					$http.post('/login',user)
					.success(function(data){
						console.log(data)
					}).error(function(data,status){
						// TODO: do something on error. AND on facebook login error
					})
				}
			})
		}
}])