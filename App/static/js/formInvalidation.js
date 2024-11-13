document.addEventListener("DOMContentLoaded", function () {
    function initializeFormValidation(formSelector) {
        var forms = document.querySelectorAll(formSelector);

        // Loop sobre os formulários e aplicar a validação
        Array.prototype.slice.call(forms).forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }
    // Chame a função para inicializar a validação em todos os formulários
    initializeFormValidation(".form-area, .form-curso, .form-equipamento, .form-relatorio, .form-ocupado, .form-reserva, .form-sala, .form-funcionario");
});
