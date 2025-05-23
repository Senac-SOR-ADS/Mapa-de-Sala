document.addEventListener('DOMContentLoaded', function () {

    /* ===================== Função de Validação ===================== */
    function applyValidation(input, isValid) {
        input.classList.toggle('is-valid', isValid);
        input.classList.toggle('is-invalid', !isValid);
    }

    /* ===================== Validação de Data ===================== */
    const today = new Date();
    const currentDate = today.toISOString().split('T')[0];

    const dataNascimentoInput = document.getElementById('dataNasc');
    if (dataNascimentoInput) {
        dataNascimentoInput.max = currentDate;
        dataNascimentoInput.addEventListener('blur', (e) => {
            const datePattern = /^\d{4}-\d{2}-\d{2}$/;
            const isValid = datePattern.test(e.target.value);
            if (isValid) {
                const [year, month, day] = e.target.value.split('-').map(Number);
                const isDateValid = year >= 1900 && year <= today.getFullYear() &&
                    month >= 1 && month <= 12 &&
                    day >= 1 && day <= 31;
                const isNotFutureDate = year < today.getFullYear() ||
                    (year === today.getFullYear() && (month < today.getMonth() + 1 ||
                        (month === today.getMonth() + 1 && day <= today.getDate())));
                applyValidation(dataNascimentoInput, isDateValid && isNotFutureDate);
            } else {
                applyValidation(dataNascimentoInput, false);
            }
        });
    }

    /* ===================== Validação de E-mail ===================== */
    const emailInput = document.getElementById('email');
    if (emailInput) {
        emailInput.addEventListener('input', (e) => {
            const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            const normalizedEmail = e.target.value.toLowerCase();
            emailInput.value = normalizedEmail;
            applyValidation(emailInput, emailPattern.test(normalizedEmail));
        });
    }

    /* ===================== Validação de Telefone ===================== */
    const telefoneInput = document.getElementById('telefone');
    if (telefoneInput) {
        telefoneInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, '');
            value = value.length <= 10
                ? value.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3')
                : value.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
            telefoneInput.value = value;
            const telefonePattern = /^\(\d{2}\) \d{4,5}-\d{4}$/;
            applyValidation(telefoneInput, telefonePattern.test(value));
        });
    }

    /* ===================== Validação de CPF/CNPJ ===================== */
    const cpfCnpjInput = document.getElementById('cpfCnpj');
    if (cpfCnpjInput) {
        cpfCnpjInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, '');
            value = value.length <= 11
                ? value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
                : value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
            cpfCnpjInput.value = value;
            const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
            const cnpjPattern = /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/;
            applyValidation(cpfCnpjInput, cpfPattern.test(value) || cnpjPattern.test(value));
        });
    }

    /* ===================== Validação de Nome ===================== */
    const nomeInput = document.getElementById('nome');
    if (nomeInput) {
        nomeInput.addEventListener('input', () => {
            const regex = /^[a-zA-Z\s]+$/;
            applyValidation(nomeInput, regex.test(nomeInput.value));
        });
    }

    /* ===================== Remover Máscaras Antes de Enviar ===================== */
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            const normalizedEmail = emailInput.value.toLowerCase();
            if (!emailPattern.test(normalizedEmail)) {
                e.preventDefault();
                applyValidation(emailInput, false);
            } else {
                const telefoneInput = document.getElementById('telefone');
                const cpfCnpjInput = document.getElementById('cpfCnpj');
                if (telefoneInput) telefoneInput.value = telefoneInput.value.replace(/\D/g, '');
                if (cpfCnpjInput) cpfCnpjInput.value = cpfCnpjInput.value.replace(/\D/g, '');
            }
        });
    }

    /* ===================== Busca Dinâmica de Resultados ===================== */
    const searchInput = document.querySelector('.input');
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            const searchQuery = searchInput.value.trim();
            const form = searchInput.closest('form');
            const url = new URL(form.action);

            if (searchQuery.length > 0) {
                url.searchParams.set('search', searchQuery);
            } else {
                url.searchParams.delete('search');
            }

            window.history.pushState({}, '', url);

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    const newRows = new DOMParser().parseFromString(html, 'text/html').querySelector('tbody');
                    document.querySelector('tbody').innerHTML = newRows.innerHTML;

                    const tableContainer = document.getElementById('tableContainer');
                    if (searchQuery.length > 0) {
                        tableContainer.classList.remove('d-none');
                        localStorage.setItem('tableVisible', 'true');
                    } else {
                        tableContainer.classList.add('d-none');
                        localStorage.setItem('tableVisible', 'false');
                    }
                })
                .catch(error => console.error('Erro ao buscar:', error));
        });
    }

    /* ===================== Limpar Busca ===================== */
    const clearButton = document.querySelector('#clearSearch');
    if (clearButton) {
        clearButton.addEventListener('click', () => {
            searchInput.value = '';
            const form = searchInput.closest('form');
            const url = new URL(form.action);

            url.searchParams.delete('search');
            window.history.pushState({}, '', url);

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    const newRows = new DOMParser().parseFromString(html, 'text/html').querySelector('tbody');
                    document.querySelector('tbody').innerHTML = newRows.innerHTML;

                    // Oculta a tabela ao limpar a busca
                    const tableContainer = document.getElementById('tableContainer');
                    tableContainer.classList.add('d-none');
                    localStorage.setItem('tableVisible', 'false');
                })
                .catch(error => console.error('Erro ao buscar:', error));
        });
    }

    /* ===================== Exibir/Esconder Tabela e Paginação ===================== */
    document.addEventListener('DOMContentLoaded', () => {
        const toggleTableBtn = document.getElementById('toggleTable');
        const tableContainer = document.getElementById('tableContainer');
        const paginationContainer = document.getElementById('paginationContainer');

        // Inicializa a tabela oculta na primeira vez
        if (!localStorage.getItem('tableVisible')) {
            tableContainer.classList.add('d-none');
            paginationContainer.style.display = 'none';
        } else if (localStorage.getItem('tableVisible') === 'true') {
            tableContainer.classList.remove('d-none');
            paginationContainer.style.display = 'block';
        } else {
            tableContainer.classList.add('d-none');
            paginationContainer.style.display = 'none';
        }

        // Alterna visibilidade da tabela ao clicar no botão
        toggleTableBtn.addEventListener('click', () => {
            if (tableContainer.classList.contains('d-none')) {
                tableContainer.classList.remove('d-none');
                paginationContainer.style.display = 'block';
                localStorage.setItem('tableVisible', 'true');
            } else {
                tableContainer.classList.add('d-none');
                paginationContainer.style.display = 'none';
                localStorage.setItem('tableVisible', 'false');
            }
        });

        // Garante que tabela permaneça visível ao usar paginação
        document.querySelectorAll('.pagination .page-link').forEach(link => {
            link.addEventListener('click', () => {
                tableContainer.classList.remove('d-none');
                paginationContainer.style.display = 'block';
                localStorage.setItem('tableVisible', 'true');
            });
        });
    });
});
