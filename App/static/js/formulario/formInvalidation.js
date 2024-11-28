document.addEventListener("DOMContentLoaded", function () {
    // Função para aplicar a validação no campo
    function applyValidation(inputElement, isValid) {
        const feedbackElement = document.getElementById(inputElement.id + 'Feedback');

        if (isValid) {
            inputElement.classList.remove('is-invalid');
            inputElement.classList.add('is-valid');
            feedbackElement && (feedbackElement.style.display = 'none');
        } else {
            inputElement.classList.remove('is-valid');
            inputElement.classList.add('is-invalid');
            feedbackElement && (feedbackElement.style.display = 'block');
        }
    }

    // Função para inicializar a validação de formulários
    function initializeFormValidation(formSelector) {
        const forms = document.querySelectorAll(formSelector);

        forms.forEach((form) => {
            form.addEventListener('submit', (event) => {
                // Impede o envio do formulário se não for válido
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                // Aplica a validação a todos os campos do formulário
                Array.from(form.elements).forEach((input) => {
                    if (input.tagName !== 'BUTTON') {
                        applyValidation(input, input.validity.valid);
                    }
                });

                // Adiciona a classe para mostrar a validação visual
                form.classList.add('was-validated');
            });

            // Validação ao sair do campo (blur)
            Array.from(form.elements).forEach((input) => {
                if (input.tagName !== 'BUTTON') {
                    input.addEventListener('blur', () => applyValidation(input, input.validity.valid));
                }
            });
        });
    }

    // Inicializa a validação para os formulários especificados
    initializeFormValidation(".form-area, .form-curso, .form-equipamento, .form-relatorio, .form-ocupado, .form-reserva, .form-sala, .form-funcionario");
});
