$(function(){
  
  $('#eye1, #eye2').click(function(){

        var target = $(this).data('target');
       
        if($(this).hasClass('bi-eye-slash')){
           
          $(this).removeClass('bi-eye-slash');
          
          $(this).addClass('bi-eye');
          
          $(target).attr('type','text');
            
        }else{
         
          $(this).removeClass('bi-eye');
          
          $(this).addClass('bi-eye-slash');  
          
          $(target).attr('type','password');
        }
    });
});