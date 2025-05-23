document.addEventListener("DOMContentLoaded", function () {

    /* ===================== Função de Validação ===================== */
    // Aplica a validação visual (classe is-valid ou is-invalid)
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

    /* ===================== Validações ===================== */
    function validateDateOfBirth(inputElement) {
        const datePattern = /^\d{4}-\d{2}-\d{2}$/;
        const isValid = datePattern.test(inputElement.value);
        if (isValid) {
            const [year, month, day] = inputElement.value.split('-').map(Number);
            const today = new Date();
            const isDateValid = year >= 1900 && year <= today.getFullYear() &&
                month >= 1 && month <= 12 && day >= 1 && day <= 31;
            const isNotFutureDate = (year < today.getFullYear()) || 
                (year === today.getFullYear() && (month < today.getMonth() + 1 || (month === today.getMonth() + 1 && day <= today.getDate())));
            applyValidation(inputElement, isDateValid && isNotFutureDate);
        } else {
            applyValidation(inputElement, false);
        }
    }

    function validateEmail(inputElement) {
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const normalizedEmail = inputElement.value.toLowerCase();
        inputElement.value = normalizedEmail;
        applyValidation(inputElement, emailPattern.test(normalizedEmail));
    }

    function validatePhone(inputElement) {
        let value = inputElement.value.replace(/\D/g, '');
        value = value.length <= 10
            ? value.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3')
            : value.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
        inputElement.value = value;
        const phonePattern = /^\(\d{2}\) \d{4,5}-\d{4}$/;
        applyValidation(inputElement, phonePattern.test(value));
    }

    function validateCpfCnpj(inputElement) {
        let value = inputElement.value.replace(/\D/g, '');
        value = value.length <= 11
            ? value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
            : value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
        inputElement.value = value;

        const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
        const cnpjPattern = /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/;
        applyValidation(inputElement, cpfPattern.test(value) || cnpjPattern.test(value));
    }

    function validateName(inputElement) {
        const regex = /^[a-zA-Z\s]+$/;
        applyValidation(inputElement, regex.test(inputElement.value));
    }

    /* ===================== Inicialização da Validação de Formulários ===================== */
    function initializeFormValidation(formSelector) {
        const forms = document.querySelectorAll(formSelector);

        forms.forEach((form) => {
            form.addEventListener('submit', (event) => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                Array.from(form.elements).forEach((input) => {
                    if (input.tagName !== 'BUTTON') {
                        switch (input.id) {
                            case 'dataNasc':
                                validateDateOfBirth(input);
                                break;
                            case 'email':
                                validateEmail(input);
                                break;
                            case 'telefone':
                                validatePhone(input);
                                break;
                            case 'cpfCnpj':
                                validateCpfCnpj(input);
                                break;
                            case 'nome':
                                validateName(input);
                                break;
                            default:
                                applyValidation(input, input.validity.valid);
                        }
                    }
                });

                form.classList.add('was-validated');
            });

            Array.from(form.elements).forEach((input) => {
                if (input.tagName !== 'BUTTON') {
                    input.addEventListener('blur', () => {
                        switch (input.id) {
                            case 'dataNasc':
                                validateDateOfBirth(input);
                                break;
                            case 'email':
                                validateEmail(input);
                                break;
                            case 'telefone':
                                validatePhone(input);
                                break;
                            case 'cpfCnpj':
                                validateCpfCnpj(input);
                                break;
                            case 'nome':
                                validateName(input);
                                break;
                            default:
                                applyValidation(input, input.validity.valid);
                        }
                    });
                }
            });
        });
    }

    /* ===================== Inicializa a Validação para Formulários ===================== */
    initializeFormValidation(".form-area, .form-curso, .form-equipamento, .form-relatorio, .form-ocupado, .form-reserva, .form-sala, .form-funcionario");

});
