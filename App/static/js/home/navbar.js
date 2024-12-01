// Seleção dos elementos necessários
const navbarToggler = document.querySelector('.navbar-toggler');
const menu = document.querySelector('#navbarNav');

// Função para alternar o estado do menu
function toggleNavbar() {
    navbarToggler.classList.toggle('collapsed');
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

// Função para garantir que o menu esteja fechado ao clicar fora do menu
document.addEventListener('click', function (event) {
    if (!navbarToggler.contains(event.target) && !menu.contains(event.target)) {
        if (menu.classList.contains('show')) {
            menu.classList.remove('show');
            navbarToggler.setAttribute('aria-expanded', 'false');
        }
    }
});

// Função para controlar o comportamento do menu dropdown
const dropdownItems = document.querySelectorAll('.nav-item.dropdown');
dropdownItems.forEach(function (item) {
    item.addEventListener('mouseover', function () {
        const dropdownMenu = item.querySelector('.dropdown-menu');
        dropdownMenu.style.display = 'block';
        dropdownMenu.style.opacity = 1;
    });
    
    item.addEventListener('mouseout', function () {
        const dropdownMenu = item.querySelector('.dropdown-menu');
        dropdownMenu.style.display = 'none';
        dropdownMenu.style.opacity = 0;
    });
});
