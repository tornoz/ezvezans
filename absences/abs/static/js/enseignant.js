$(window).ready(function() {
    $('.add_absence').click(function() {
        console.log("requete ajax :");
        var div = $(this).parent().find('.absence_container');
        var ajaxLoader = $(document.createElement('img'));
        ajaxLoader.attr('src', "/static/img/ajax-loader.gif");
        div.append(ajaxLoader);
        $.get( "ajax/absent/" + $(this).parent().parent().attr('id'), function( data ) {
            var etudiants = data.split(';');
            var select = $(document.createElement('select'));
            for(var i = 0; i<etudiants.length-1; i++) {
               
                var str = '<option value="'+etudiants[i]+'">'+etudiants[i]+'</option>';
                 console.log(str);
                 ajaxLoader.remove();
                select.append(str);
            }
            div.append('<li>')
            div.append(select);
            div.append('</li>');
            
        });
    });

});
