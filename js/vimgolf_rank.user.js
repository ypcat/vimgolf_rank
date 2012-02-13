// ==UserScript==
// @name           vimgolf_rank
// @namespace      http://vimgolf-rank.appspot.com/
// @include        http://vimgolf.com/*
// @include        http://www.vimgolf.com/*
// @require        http://code.jquery.com/jquery.min.js
// ==/UserScript==

//XXX use first one for deploy
//var feed_url = "http://vimgolf-rank.appspot.com/json";
var feed_url = "http://localhost:8080/json";

if(window.location.pathname == '/'){
    GM_xmlhttpRequest({
        method:"GET",
        url:feed_url+'/challenges',
        onload:function(response){
            challenges = eval('('+response.responseText+')');
            $('h5').each(function(){
                var handle = $(this).find('a').attr('href').split('/')[2];
                if(handle in challenges)
                    $(this).append(', '+challenges[handle].active_golfers+' active golfers');
            });
        }
    });
}
else if(window.location.pathname == '/top'){
    GM_xmlhttpRequest({
        method:"GET",
        url:feed_url+'/top',
        onload:function(response){
            golfers = eval('('+response.responseText+')');
            $('h6').each(function(){
                var handle = $(this).find('a').text().slice(1);
                if(handle in golfers)
                    $(this).append('<p>Global rank '+golfers[handle].global_rank+'</p>');
            });
        }
    });
}

