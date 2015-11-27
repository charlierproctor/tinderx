'use strict';

angular.module('tinderX',[
	'ui.router',
	'tinderX.login'
]).

config(['$urlRouterProvider', function($urlRouterProvider) {
	$urlRouterProvider.otherwise("/");
}])
