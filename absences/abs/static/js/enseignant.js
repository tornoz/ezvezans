$(window).ready(function() {
    $('.add_absence').click(function() {
        console.log("requete ajax :");
        var div = $(this).parent().find('.absence_container');
        var ajaxLoader = $(document.createElement('img'));
        ajaxLoader.attr('src', "/static/img/ajax-loader.gif");
        var coursId = $(this).parent().parent().attr('id');
        div.append(ajaxLoader);
        $.get( "ajax/absent/" + coursId, function( data ) {
            var etudiants = data.split(';');
            var select = $(document.createElement('select'));
            for(var i = 0; i<etudiants.length-1; i++) {
                var names = etudiants[i].split(",");
                var str = '<option value="'+names[1]+'">'+names[0]+'</option>';
                 console.log(str);
                 ajaxLoader.remove();
                select.append(str);
            }
            var list_elem = $(document.createElement('li'));
            list_elem.append(select);
            var img_rm = $(document.createElement('img'));
            img_rm.attr('class', 'rm_select');
            img_rm.attr('src', "/static/img/delete.png");
            var img_ok = $(document.createElement('img'));
            img_ok.attr('class', 'ok_select');
            img_ok.attr('src', "/static/img/check.png");
            list_elem.append(img_rm);
            list_elem.append(img_ok);
            div.append(list_elem);
            img_rm.click(function() {
                list_elem.remove();
            });
            var etudiantid = img_ok.parent().find('select').val();
            var etudiant_name = img_ok.parent().find('select option:selected').text();
            img_ok.click(function() {
                 $.get( "ajax/insert/absent/" + coursId + '/' + etudiantid, function( data ) {
                    if(data == "ok") {
                        div.parent().find('.abs_list').append('<li>'+etudiant_name+'</li>');
                    }
                 });
            });
            
        });
    });
    
    $('.rm_absence').click(function() {
        var absenceid = $(this).parent().attr('id').replace('a', '');
        var node = $(this).parent();
        $.get( "ajax/delete/absent/" + absenceid, function( data) {
                    if(data == "ok") {
                        console.log("COUCOU");
                        node.remove();
                    }
                 });
    });

});
