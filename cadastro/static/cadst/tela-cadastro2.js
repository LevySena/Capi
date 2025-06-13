$(function(){
  
  $('#eye').click(function(){
       
        if($(this).hasClass('bi-eye-slash')){
           
          $(this).removeClass('bi-eye-slash');
          
          $(this).addClass('bi-eye');
          
          $('#senha').attr('type','text');
            
        }else{
         
          $(this).removeClass('bi-eye');
          
          $(this).addClass('bi-eye-slash');  
          
          $('#senha').attr('type','password');
        }
    });
});