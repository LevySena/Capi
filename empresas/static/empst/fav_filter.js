document.addEventListener('DOMContentLoaded', function() {
    const showFavoritesCheckbox = document.getElementById('favoritas');

    if (showFavoritesCheckbox) {
        showFavoritesCheckbox.addEventListener('change', function() {
            const currentUrl = new URL(window.location.href);
            
            if (this.checked) {
                currentUrl.searchParams.set('favoritas_apenas', 'true');
            } else {
                currentUrl.searchParams.delete('favoritas_apenas');
            }
            
            window.location.href = currentUrl.toString(); 
        });
    }
});