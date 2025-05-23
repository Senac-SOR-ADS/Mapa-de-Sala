document.addEventListener("DOMContentLoaded", function() {
    const dropdownItems = document.querySelectorAll('.nav-item.dropdown');
    
    dropdownItems.forEach(item => {
        const dropdownMenu = item.querySelector('.dropdown-menu');
        
        item.addEventListener('mouseenter', function() {
            dropdownMenu.style.display = 'block';
            dropdownMenu.style.opacity = 1;
        });

        item.addEventListener('mouseleave', function() {
            dropdownMenu.style.display = 'none';
            dropdownMenu.style.opacity = 0;
        });
    });

    window.addEventListener('resize', handleResize);
    handleResize();
});
