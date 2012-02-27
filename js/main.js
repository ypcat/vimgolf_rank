function beautify_globalrank()
{
    (function($){})(jQuery);
    $("tr:even").addClass("top-even");
    $("tr.top").each(function(index) {
        var global_rank = $('td.global_rank',$(this)).html();
        // Assume the global_rank is sorted
        var rank = index+1;
        // Special case: two people have the same global_rank should have the same rank 
        var prev_global_rank = $(this).prev().find('td.global_rank').text();
        if (global_rank==prev_global_rank) {
            rank = $(this).prev().find('td.rank').text();
        }
        $("td.rank",$(this)).text(rank);
    });
}
