'use strict';

angular.module('tinderX.swipeable',[])
.directive('swipeable', ['$swipe',function($swipe){
	return {
		restrict: 'A',
		link: function(scope,elem,attrs){

			elem.css({
                position: 'absolute',
                top: 0,
				left: 0,
				'-webkit-user-drag': 'none'
            });

			var start
			var orig = {
				x: elem.prop('offsetLeft'),
				y: elem.prop('offsetTop')
			}

			$swipe.bind(elem,{
				start: function(coords,event){
					start = {
						x: coords.x,
						y: coords.y
					}
				},
				move: function(coords,event){
					elem.css({
						top: (orig.y + coords.y - start.y) + "px",
						left: (orig.x + coords.x - start.x) + "px"
					})
				},
				cancel: function(event){
					elem.css({
						top: orig.y + "px",
						left: orig.x + "px"
					})
				},
				end: function(coords,event){
					elem.css({
						top: orig.y + "px",
						left: orig.x + "px"
					})
				}
			})

		}
	}
}])