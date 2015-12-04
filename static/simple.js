/**
 * Created by sebastian.kouba on 12/4/2015.
 */
$('table').tablesorter({
    theme: 'blue'
});

    $("tr").not('tablesorter-childRow').on('click', function(){
        $(this).next().toggleClass('hide');
    });

    $("#toggle-invisible-woman").on('click', function(){
        $("#invisible-woman").toggleClass('hide');
    });