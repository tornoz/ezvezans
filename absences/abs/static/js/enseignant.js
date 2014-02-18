$(window).ready(function() {
    $('.add_absence').click(function() {
        
        //Contains the saved absences
        var abs_container = $(this).parent().find('.absence_container');
        //Gif
        var ajaxLoader = $(document.createElement('img'));
        ajaxLoader.attr('src', "/static/img/ajax-loader.gif");
        //Id of the cours
        var coursId = $(this).parent().parent().attr('id');
        //Set the loader
        abs_container.append(ajaxLoader);
        //Call the ajac function
        $.get( "ajax/absent/" + coursId, function( data ) {
            //on success :
            var etudiants = data.split(';');
            //Create select element
            var select = $(document.createElement('select'));
            select.addClass('etudiantSelector');
            //put th values into it
            for(var i = 0; i<etudiants.length-1; i++) {
                var names = etudiants[i].split(",");
                var str = '<option value="'+names[1]+'">'+names[0]+'</option>';
                 console.log(str);
                 ajaxLoader.remove();
                select.append(str);
            }
            //Create the list element and append it the select and buttons
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
            //Add the element to the list
            abs_container.append(list_elem);
            img_rm.click(function() {
                list_elem.remove();
            });
           img_ok.click(function() {
                 var etudiantid = img_ok.parent().find('.etudiantSelector').val();
                 $.get( "ajax/insert/absent/" + coursId + '/' + etudiantid, function( data ) {
                    if(data != "error") {
                        var etudiant_name = img_ok.parent().find('.etudiantSelector option:selected').text();
                        var img = $(document.createElement('img'));
                        img.addClass('rm_absence');
                        img.attr('src', '/static/img/delete.png');
                        img.click(rm_absence);
                        var abslist = abs_container.parent().find('.abs_list');
                        var li = $(document.createElement('li'));
                        li.attr('id', 'a' + data);
                        li.append(etudiant_name);
                        li.append(img);
                        abslist.append(li);
                        img_rm.click();
                    }
                 });
            });
            
        });
    });
    
    var rm_absence = function() {
        var absenceid = $(this).parent().attr('id').replace('a', '');
        var node = $(this).parent();
        $.get( "ajax/delete/absent/" + absenceid, function( data) {
                    if(data == "ok") {
                        console.log("COUCOU");
                        node.remove();
                    }
                 });
    };
    
    $('.rm_absence').click(rm_absence);

});
