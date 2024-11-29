// Seleção dos elementos necessários
const navbarToggler = document.querySelector('.navbar-toggler');
const menu = document.querySelector('.navbar-collapse');

// Função para alternar o estado do menu
function toggleNavbar() {
    navbarToggler.classList.toggle('open');
    if (menu) {
        menu.classList.toggle('show');
    }
    updateAriaExpanded();
}

// Função para atualizar o atributo "aria-expanded"
function updateAriaExpanded() {
    const isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
    navbarToggler.setAttribute('aria-expanded', !isExpanded);
}

// Adiciona o evento de clique no botão de alternância
navbarToggler.addEventListener('click', toggleNavbar);

// Caso o menu seja fechado ao clicar fora dele
document.addEventListener('click', (event) => {
    const clickedOutside = !navbarToggler.contains(event.target) && !menu.contains(event.target);
    if (clickedOutside && navbarToggler.classList.contains('open')) {
        toggleNavbar();
    }
});

// Fecha o menu ao pressionar "Escape"
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navbarToggler.classList.contains('open')) {
        toggleNavbar();
    }
});
