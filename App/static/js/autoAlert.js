// Função para fazer o alerta desaparecer após um tempo
function dismissAlerts() {
    const alerts = document.querySelectorAll('.auto-dismiss');
    alerts.forEach(alert => {
        alert.addEventListener('animationend', () => {
            alert.remove();
        });
    });
}
// Ao carregar o conteúdo, iniciar o desaparecimento dos alertas
document.addEventListener("DOMContentLoaded", function () {
    dismissAlerts();
});
