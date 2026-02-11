document.addEventListener("DOMContentLoaded", function () {
    const mudarSenhaBtn = document.getElementById("mudarSenhaBtn");
    const salvarSenhaBtn = document.getElementById("salvarSenhaBtn");
    const alterarSenhaModal = new bootstrap.Modal(document.getElementById("alterarSenhaModal"));
    const senhaInput = document.getElementById("passwordInput");
    const confirmSenhaInput = document.getElementById("confirmPasswordInput");
    const senhaHiddenInput = document.getElementById("senhaInput");
    const passwordStrength = document.getElementById("passwordStrength");
    const themeToggleBtn = document.getElementById("theme-toggle-btn");
    const togglePasswordBtn = document.getElementById("togglePassword");
    const togglePasswordIcon = togglePasswordBtn.querySelector("i");
    const togglePasswordText = togglePasswordBtn.querySelector("span");

    // Exibir modal de alteração de senha
    mudarSenhaBtn.addEventListener("click", () => alterarSenhaModal.show());

    // Alternar visibilidade da senha
    togglePasswordBtn.addEventListener("click", function () {
        const isPasswordVisible = senhaInput.type === "text";
        senhaInput.type = confirmSenhaInput.type = isPasswordVisible ? "password" : "text";
        togglePasswordIcon.classList.toggle("bi-eye-slash", !isPasswordVisible);
        togglePasswordIcon.classList.toggle("bi-eye", isPasswordVisible);
        togglePasswordText.textContent = isPasswordVisible ? "Mostrar Senha" : "Ocultar Senha";
    });

    // Verificar força da senha
    senhaInput.addEventListener("input", function () {
        const senha = senhaInput.value;
        let forca = 0;

        if (senha.length >= 8) forca += 25;
        if (/[A-Z]/.test(senha)) forca += 25;
        if (/[0-9]/.test(senha)) forca += 25;
        if (/[^a-zA-Z0-9]/.test(senha)) forca += 25;

        passwordStrength.style.width = forca + "%";
        passwordStrength.className = "progress-bar";
        passwordStrength.classList.add(forca < 50 ? "bg-danger" : forca < 75 ? "bg-warning" : "bg-success");
    });

    // Validação de senha
    function validarSenha(password, confirmPassword) {
        if (!password || !confirmPassword) return exibirErro("Por favor, preencha todos os campos.");
        if (password !== confirmPassword) return exibirErro("As senhas não coincidem!");
        if (password.length < 8) return exibirErro("A senha deve ter pelo menos 8 caracteres!");
        return true;
    }

    // Exibir mensagens de erro no modal
    function exibirErro(mensagem) {
        const alertBox = document.getElementById("senhaErro");
        alertBox.innerHTML = mensagem;
        alertBox.classList.remove("d-none");
        setTimeout(() => alertBox.classList.add("d-none"), 3000);
        return false;
    }

    // Habilitar botão de salvar apenas se as senhas coincidirem
    function validarSenhas() {
        salvarSenhaBtn.disabled = !(senhaInput.value.length >= 8 && senhaInput.value === confirmSenhaInput.value);
    }

    senhaInput.addEventListener("input", validarSenhas);
    confirmSenhaInput.addEventListener("input", validarSenhas);

    // Salvar nova senha após validação
    salvarSenhaBtn.addEventListener("click", function () {
        if (validarSenha(senhaInput.value, confirmSenhaInput.value)) {
            senhaHiddenInput.value = senhaInput.value;
            document.getElementById("alterarSenhaForm").submit();
            alterarSenhaModal.hide();
        }
    });

    // Alternar tema claro/escuro
    themeToggleBtn.addEventListener("click", function (event) {
        document.body.classList.toggle("dark-mode");
        document.querySelectorAll("#profile-card, #alterarSenhaModal, .modal-content").forEach(el => el.classList.toggle("dark-mode"));
        const isDarkMode = document.body.classList.contains("dark-mode");
        event.target.innerHTML = isDarkMode ? "☀️" : "🌙";
        event.target.style.color = isDarkMode ? "#FFD700" : "#4b6e8e";
        localStorage.setItem("darkMode", isDarkMode);
    });

    // Restaurar preferência do tema
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
        document.querySelectorAll("#profile-card, #alterarSenhaModal, .modal-content").forEach(el => el.classList.add("dark-mode"));
        themeToggleBtn.innerHTML = "☀️";
        themeToggleBtn.style.color = "#FFD700";
    }
});
