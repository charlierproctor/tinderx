'use strict';

angular.module('tinderX.swipeable',[])
.directive('swipeable', ['$swipe',function($swipe){
	return {
		restrict: 'A',
		link: function(scope,elem,attrs){

			elem.css({
                position: 'absolute'
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