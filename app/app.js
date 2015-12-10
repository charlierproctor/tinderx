'use strict';

angular.module('tinderX',[
	'ui.router',
	'tinderX.login',
	'tinderX.swipe',
	'facebook',
	'ngCookies',
	'gajus.swing'
]).

config(['$urlRouterProvider', 'FacebookProvider', 
	function($urlRouterProvider, fbProvider) {
		$urlRouterProvider.otherwise("/");
		fbProvider.init('1658892404386340')
}])