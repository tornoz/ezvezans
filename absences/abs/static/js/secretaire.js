 
 $(window).ready(function() {
    var rm_justificatif = function() {
        var justid = $(this).parent().parent().attr('id').replace('j', '');
        var node = $(this).parent().parent();
        $.get( "ajax/delete/justificatif/" + justid, function( data) {
                    if(data == "ok") {
                        node.remove();
                    }
                 });
    };
    
    $('.rm_justificatif').click(rm_justificatif);
});
