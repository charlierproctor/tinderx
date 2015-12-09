'use strict';

angular.module('tinderX.login', ['ui.router'])

.config(['$stateProvider',function($stateProvider){
	$stateProvider.state('login', {
		url: '/',
		templateUrl: 'partials/login.html',
		controller: 'LoginCtrl'
	})
}])

.controller('LoginCtrl', ['$scope', 'Facebook', function($scope, fb){
	$scope.login = function() {
		fb.login(function(res) {
			console.log(res)
		})
	}
}])