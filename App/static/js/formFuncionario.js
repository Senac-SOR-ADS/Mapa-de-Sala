document.addEventListener('DOMContentLoaded', function () {
    // Função para aplicar validação a um campo específico
    function applyValidation(input, isValid) {
        if (isValid) {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        } else {
            input.classList.remove('is-valid');
            input.classList.add('is-invalid');
        }
    }

    // Definir o valor máximo de data para o ano atual
    const currentYear = new Date().getFullYear();
    const today = new Date();
    const currentMonth = today.getMonth() + 1;
    const currentDay = today.getDate();
    const currentDate = `${currentYear}-${String(currentMonth).padStart(2, '0')}-${String(currentDay).padStart(2, '0')}`;

    const dataNascimentoInput = document.getElementById('dataNasc');

    // Ajustar o atributo max dinamicamente para o dia atual
    if (dataNascimentoInput) {
        dataNascimentoInput.max = currentDate;
    }

    // Validação de Data de Nascimento
    dataNascimentoInput?.addEventListener('blur', (e) => {
        const datePattern = /^\d{4}-\d{2}-\d{2}$/;
        const isValid = datePattern.test(e.target.value);

        if (isValid) {
            const [year, month, day] = e.target.value.split('-').map(Number);

            // Verifica se o ano, mês e dia são válidos
            const isDateValid =
                year >= 1900 && 
                year <= currentYear && 
                month >= 1 && month <= 12 && 
                day >= 1 && day <= 31;

            // Verifica se a data não é no futuro
            const isNotFutureDate =
                (year < currentYear) || 
                (year === currentYear && (month < currentMonth || (month === currentMonth && day <= currentDay)));

            // Aplica a validação
            applyValidation(dataNascimentoInput, isDateValid && isNotFutureDate);
        } else {
            applyValidation(dataNascimentoInput, false);
        }
    });


    // Validação e formatação do Email
    const emailInput = document.getElementById('email');
    emailInput?.addEventListener('input', (e) => {
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const normalizedEmail = e.target.value.toLowerCase();
        const isValid = emailPattern.test(normalizedEmail);

        emailInput.value = normalizedEmail;
        applyValidation(emailInput, isValid);
    });

    // Validação e formatação do Telefone
    const telefoneInput = document.getElementById('telefone');
    telefoneInput?.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        value = value.length <= 10
            ? value.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3')
            : value.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
        telefoneInput.value = value;

        const telefonePattern = /^\(\d{2}\) \d{4,5}-\d{4}$/;
        applyValidation(telefoneInput, telefonePattern.test(value));
    });

    // Validação e formatação do CPF/CNPJ
    const cpfCnpjInput = document.getElementById('cpfCnpj');
    cpfCnpjInput?.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        value = value.length <= 11
            ? value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
            : value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
        cpfCnpjInput.value = value;

        const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
        const cnpjPattern = /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/;
        applyValidation(cpfCnpjInput, cpfPattern.test(value) || cnpjPattern.test(value));
    });

    // Remover máscaras antes de enviar o formulário
    document.querySelector('form')?.addEventListener('submit', (e) => {
        telefoneInput.value = telefoneInput.value.replace(/\D/g, '');
        cpfCnpjInput.value = cpfCnpjInput.value.replace(/\D/g, '');
        emailInput.value = emailInput.value.toLowerCase();
    });

    // Validação do nome (apenas letras e espaços)
    const nomeInput = document.getElementById('nome');
    nomeInput?.addEventListener('input', function () {
        const regex = /^[a-zA-Z\s]+$/;
        const isValid = regex.test(nomeInput.value);
        applyValidation(nomeInput, isValid);
    });

    // Validação do nome ao sair do campo (blur)
    nomeInput?.addEventListener('blur', function () {
        const regex = /^[a-zA-Z\s]+$/;
        const isValid = regex.test(nomeInput.value);
        applyValidation(nomeInput, isValid);
    });
});
