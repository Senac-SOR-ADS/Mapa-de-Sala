document.addEventListener('DOMContentLoaded', function() {
    // Função para remover o alerta
    function removeAlert(alertElement) {
        // Começar a animação de fade-out
        alertElement.style.transition = 'opacity 0.5s ease, visibility 0s 0.5s';
        alertElement.style.opacity = '0';
        alertElement.style.visibility = 'hidden';

        // Após a animação de fade-out, removemos o elemento da DOM
        setTimeout(() => {
            alertElement.remove();

            // Verificar se não há mais alertas visíveis
            const remainingAlerts = document.querySelectorAll('.alert-container .alert');
            if (remainingAlerts.length === 0) {
                // Se não houver alertas, esconder o contêiner de alertas
                document.querySelector('.alert-container').classList.add('empty');
            }
        }, 500);
    }

    // Adicionar evento de clique no botão de fechamento
    const closeButtons = document.querySelectorAll('.custom-close-btn');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.alert');
            removeAlert(alert);
        });
    });

    // Remover alertas automaticamente
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.classList.add('auto-dismiss');
        setTimeout(() => {
            removeAlert(alert);
        }, 2000);
    });
});
