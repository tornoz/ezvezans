$(window).ready(function() {
   $('.tab').each(function() {
       $('#tabs').append("<a href='#" + $(this).attr('id') + "'>" + $(this).attr("tab_name") + "</a> ");
   });
   
   var hash = window.location.hash;
   if(hash != "") {
       $(hash).show();
       $(hash).addClass('displayed');
       $('#tabs a').each(function() {
            if($(this).attr('href') == hash) {
                $(this).addClass('displayed');
            }
        });
   }
   else {
        $('.tab').first().show();
        $('.tab').first().addClass('displayed');
        $('#tabs a').first().addClass('displayed');
    }
   
   
   
   $('#tabs a').click(function() {
       var tabid = $(this).attr('href');
       var tab = $(this);
       $('.tab.displayed').slideUp('fast', function() {
           $(tabid).slideDown();
           $('.tab.displayed').removeClass('displayed');
           $('#tabs a.displayed').removeClass('displayed');
           $(tabid).addClass('displayed');
           $(tab).addClass('displayed');
        });
       
   });
    
});
