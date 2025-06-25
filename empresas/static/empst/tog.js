document.addEventListener('DOMContentLoaded', function() {
    const favoriteCheckbox = document.getElementById('favorito');
    const statusMessageDiv = document.getElementById('status-message');
    
    if (favoriteCheckbox) {
        favoriteCheckbox.addEventListener('change', function() {
            const empresaId = this.dataset.empresaId; // Pega o ID da empresa do atributo data-
            const isChecked = this.checked; // Verifica se o checkbox está marcado ou desmarcado

            statusMessageDiv.className = ''; // Limpa classes anteriores
            statusMessageDiv.textContent = 'Atualizando...'; // Mensagem de feedback

            // Envia a requisição AJAX
            fetch('/empresas/tog/', { // Ajuste a URL se necessário (e.g., /meuapp/toggle_favorite/)
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Obtém o token CSRF
                },
                body: JSON.stringify({
                    'empresa_id': empresaId,
                    'favoritada': isChecked
                })
            })
            .then(response => response.json()) // Converte a resposta para JSON
            .then(data => {
                if (data.status === 'success') {
                    statusMessageDiv.className = 'success';
                    statusMessageDiv.textContent = data.message;
                } else {
                    statusMessageDiv.className = 'error';
                    statusMessageDiv.textContent = data.message;
                    // Se houve erro no backend, reverte o estado do checkbox
                    favoriteCheckbox.checked = !isChecked; 
                }
            })
            .catch(error => {
                console.error('Erro na requisição:', error);
                statusMessageDiv.className = 'error';
                statusMessageDiv.textContent = 'Erro ao conectar com o servidor.';
                // Reverte o estado do checkbox em caso de erro de rede ou falha inesperada
                favoriteCheckbox.checked = !isChecked;
            });
        });
    }

    // Função auxiliar para obter o token CSRF do cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});