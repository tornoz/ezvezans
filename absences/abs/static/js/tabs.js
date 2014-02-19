$(window).ready(function() {
   $('.tab').each(function() {
       $('#tabs').append("<a href='#" + $(this).attr('id') + "'>" + $(this).attr("tab_name") + "</a> ");
   });
   
   $('.tab').first().show();
   $('.tab').first().addClass('displayed');
   
   $('#tabs a').click(function() {
       var tabid = $(this).attr('href');
       $('.displayed').slideUp('fast', function() {
           $(tabid).slideDown();
           $('.displayed').removeClass('displayed');
       $(tabid).addClass('displayed');
        });
       
   });
    
});
