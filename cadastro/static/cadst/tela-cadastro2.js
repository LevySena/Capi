
document.addEventListener('DOMContentLoaded', function() {
    const cpfInput = document.getElementById('id_cpf'); // Ou id_cpf_opcao2, dependendo do campo que você quer formatar
    
    if (cpfInput) {
        cpfInput.addEventListener('input', function (e) {
            let value = e.target.value;
            value = value.replace(/\D/g, ''); 

            if (value.length > 9) {
                value = value.replace(/^(\d{3})(\d{3})(\d{3})(\d{2}).*/, '$1.$2.$3-$4');
            } else if (value.length > 6) {
                value = value.replace(/^(\d{3})(\d{3})(\d{3}).*/, '$1.$2.$3');
            } else if (value.length > 3) {
                value = value.replace(/^(\d{3})(\d{3}).*/, '$1.$2');
            }
            
            e.target.value = value.substring(0, 14);
        });

        if (cpfInput.value) {
            let initialValue = cpfInput.value;
            initialValue = initialValue.replace(/\D/g, ''); 
            if (initialValue.length > 9) {
                initialValue = initialValue.replace(/^(\d{3})(\d{3})(\d{3})(\d{2}).*/, '$1.$2.$3-$4');
            } else if (initialValue.length > 6) {
                initialValue = initialValue.replace(/^(\d{3})(\d{3})(\d{3}).*/, '$1.$2.$3');
            } else if (initialValue.length > 3) {
                initialValue = initialValue.replace(/^(\d{3})(\d{3}).*/, '$1.$2');
            }
            cpfInput.value = initialValue.substring(0, 14);
        }
    }
});
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
