document.addEventListener('DOMContentLoaded', () => {
    // Referências ao DOM
    const emailField = document.getElementById('email');
    const rememberCheckbox = document.getElementById('lembrar');
    const message = document.getElementById('message');
    const senhaInput = document.getElementById('senha');
    const toggleSenhaBtn = document.getElementById('toggleSenha');
    const emailHelp = document.getElementById('emailHelp');

    // Função para exibir mensagens estilizadas
    function showMessage(text, color = '#4caf50') {
        message.textContent = text;
        message.style.color = color;
        message.classList.remove('hidden');
        message.classList.add('visible');

        // Ocultar a mensagem após 3 segundos
        setTimeout(() => {
            message.classList.remove('visible');
            message.classList.add('hidden');
        }, 3000);
    }

    // Função para exibir mensagens no campo de ajuda do e-mail
    function showEmailMessage(messageText, color = '#4caf50') {
        emailHelp.textContent = messageText;
        emailHelp.style.color = color;
    }

    // Função para salvar o e-mail no localStorage
    function saveCredentials() {
        if (rememberCheckbox.checked) {
            const email = emailField.value.trim();
            if (email && validateEmail(email)) {
                localStorage.setItem('email', email);
                localStorage.setItem('rememberMe', 'true');
                showMessage('Lembrar-me ativado!');
            } else {
                showMessage('Por favor, insira um e-mail válido.', '#ff5722');
            }
        } else {
            localStorage.removeItem('email');
            localStorage.removeItem('rememberMe');
            showMessage('Lembrar-me desativado!', '#ff5722');
        }
    }

    // Função para carregar o e-mail ao inicializar a página
    function loadCredentials() {
        if (localStorage.getItem('rememberMe') === 'true') {
            rememberCheckbox.checked = true;
            emailField.value = localStorage.getItem('email') || '';
            showMessage('Bem-vindo de volta!');
        }
    }

    // Função para validar o e-mail com uma expressão regular simples
    function validateEmail(email) {
        const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return regex.test(email);
    }

    // Evento para validar o e-mail enquanto o usuário digita
    emailField.addEventListener('input', () => {
        const email = emailField.value.trim();
        if (email && validateEmail(email)) {
            showEmailMessage('Estamos prontos para a autenticação.', '#4caf50');
        } else {
            showEmailMessage('Por favor, insira um e-mail válido.', '#ff5722');
        }
    });

    // Evento para alternar a visibilidade da senha
    toggleSenhaBtn.addEventListener('click', () => {
        // Alternar o tipo do campo
        if (senhaInput.type === 'password') {
            senhaInput.type = 'text';
            toggleSenhaBtn.classList.remove('fa-eye');
            toggleSenhaBtn.classList.add('fa-eye-slash');
        } else {
            senhaInput.type = 'password';
            toggleSenhaBtn.classList.remove('fa-eye-slash');
            toggleSenhaBtn.classList.add('fa-eye');
        }
    });

    // Carregar e-mail e credenciais ao inicializar a página
    loadCredentials();

    // Evento para salvar as credenciais quando o checkbox "lembrar-me" mudar
    rememberCheckbox.addEventListener('change', saveCredentials);
});
