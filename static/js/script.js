// srcset polyfill
(function(e,t){function s(e){if(!e.attributes['srcset'])return false;var t=e.attributes['srcset'].nodeValue.split(',');for(var s=0;s<t.length;s++){var o=t[s].match(/^\s*([^\s]+)\s*(\s(\d+)w)?\s*(\s(\d+)h)?\s*(\s(\d+)x)?\s*$/),u=o[1],a=o[3]||false,f=o[5]||false,l=o[7]||1;if(a&&a>n){continue}if(f&&f>r){continue}if(l&&l>i){continue}e.src=u}}if('srcset'in t.createElement('img'))return true;var n=e.innerWidth>0?e.innerWidth:screen.width,r=e.innerHeight>0?e.innerHeight:screen.height,i=e.devicePixelRatio||1;var o=t.getElementsByTagName('img');for(var u=0;u<o.length;u++){s(o[u])}})(window,document);

// Media Breakpoint Event
(function($) {

	var $window = $(window);
	var bp_names = ['sm', 'md', 'lg'];
	var bp_current = 0;

	function bp_trigger(index) {
		if(index != 0 && bp_current == index)
			return;
		bp_current = index;
		$window.trigger('mediabreakpoint', [index, bp_names[index]]);
	}

	$window.on('resize load', function(event) {
		var width = $('.container:first').css('width');
		switch(true) {
			case width == '1012px': bp_trigger(2); break;
			case width == '752px': 	bp_trigger(1); break;
			default: 				bp_trigger(0); break;
		}
	}).trigger('resize');

})(jQuery);

// Home
(function($) {

	var $body = $('body');

	if(!$body.hasClass('home')) 
		return;

	var $window = $(window);

	var $header = $('body > header');
	var $homehero = $('#home-hero');
	var $homehero_figure = $homehero.find('figure:first');
	var $homehero_content = $homehero.find('.content:first');

	$window.on('mediabreakpoint', function(event, index, name) {		
		$homehero.css('min-height', $homehero_content.height() + 64 + 'px');
		var maxHeroHeight = $body.height() - 128;
		var currentMaxHeroHeight = parseInt($homehero.css('max-height'));
		if( isNaN(currentMaxHeroHeight) || currentMaxHeroHeight > maxHeroHeight )
			$homehero.css('max-height', maxHeroHeight + 'px');
		$homehero_content.css('margin-top', - $homehero_content.height() / 2);
		$homehero_figure.css('top', - (600 - $homehero.height()) / 2 + 'px');
	});

})(jQuery);

$(document).ready(function() {
    var notice = "&copy; 2018-" + new Date().getFullYear() + " Russ 'trdwll' Treadwell. All rights reserved.";
    $('.copy').append(notice);
});