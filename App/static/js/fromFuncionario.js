// Validação e formatação do Email
document.getElementById('email').addEventListener('input', function (e) {
    const emailInput = e.target;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (emailPattern.test(emailInput.value)) {
        emailInput.classList.remove('is-invalid');
        emailInput.classList.add('is-valid');
    } else {
        emailInput.classList.remove('is-valid');
        emailInput.classList.add('is-invalid');
    }
});

// Validação e formatação do telefone
document.getElementById('telefone').addEventListener('input', function (e) {
    const telefoneInput = e.target;
    let value = telefoneInput.value.replace(/\D/g, '');

    if (value.length <= 10) {
        value = value.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
    } else {
        value = value.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
    }
    telefoneInput.value = value;

    const telefonePattern = /^\(\d{2}\) \d{4,5}-\d{4}$/;
    if (telefonePattern.test(telefoneInput.value)) {
        telefoneInput.classList.remove('is-invalid');
        telefoneInput.classList.add('is-valid');
    } else {
        telefoneInput.classList.remove('is-valid');
        telefoneInput.classList.add('is-invalid');
    }
});

// Validação e formatação do CPF ou CNPJ
document.getElementById('cpfCnpj').addEventListener('input', function (e) {
    const cpfCnpjInput = e.target;
    let value = cpfCnpjInput.value.replace(/\D/g, '');

    if (value.length <= 11) {
        value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    } else {
        value = value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
    }
    cpfCnpjInput.value = value;

    const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
    const cnpjPattern = /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/;

    if (cpfPattern.test(cpfCnpjInput.value) || cnpjPattern.test(cpfCnpjInput.value)) {
        cpfCnpjInput.classList.remove('is-invalid');
        cpfCnpjInput.classList.add('is-valid');
    } else {
        cpfCnpjInput.classList.remove('is-valid');
        cpfCnpjInput.classList.add('is-invalid');
    }
});

