$( document ).on( 'click', '.details a', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';
       var link_array = link.split('/');
       //console.log(link);
       //console.log(link_array[4]);
       if (link_array[4] === 'category') {
           $.ajax({
               url: link,
               success: function (data) {
                   //console.log('success !!!!!!!!!!!!');
                   $('.details').html(data.result);
               },
           });

           event.preventDefault();
       }
   }
});