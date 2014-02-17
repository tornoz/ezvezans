$(window).ready(function() {
    $('.add_absence').click(function() {
        console.log("requete ajax :");
        var div = $(this).parent().find('.absence_container');
        $.get( "ajax/absent/" + $(this).parent().parent().attr('id'), function( data ) {
            var etudiants = data.split(';');
            var select = $(document.createElement('select'));
            for(var i = 0; i<etudiants.length; i++) {
               
                var str = '<option value="'+etudiants[i]+'">'+etudiants[i]+'</option>';
                 console.log(str);
                select.append(str);
            }
            div.append(select);
            
        });
    });

});
