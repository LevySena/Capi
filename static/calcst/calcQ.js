document.addEventListener('DOMContentLoaded', function() {
    const select = document.querySelector('.seletor');
    const divC = document.getElementById('carCom');
    const divM = document.getElementById('motCom');
    
    function verificar(){
        if (select.value === 'carro'){
            divC.style.display = 'block';
            divM.style.display = 'none';
        }
        else if (select.value === 'moto'){
            divC.style.display = 'none';
            divM.style.display = 'block';
        }
        else{
            divC.style.display = 'none';
            divM.style.display = 'none';
        }
    }
    verificar();
    select.addEventListener('change',verificar);
  
});