'use strict';

angular.module('tinderX',[
	'ui.router',
	'tinderX.login',
	'tinderX.swipe',
	'tinderX.swipeable',
	'facebook',
	'ngCookies',
	'ngTouch'
]).

config(['$urlRouterProvider', 'FacebookProvider', 
	function($urlRouterProvider, fbProvider) {
		$urlRouterProvider.otherwise("/");
		fbProvider.init('1658892404386340')
}])