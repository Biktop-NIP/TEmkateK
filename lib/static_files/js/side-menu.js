const sideMenuOpen = document.querySelectorAll('.js-side-menu-open');

if (sideMenuOpen.length > 0){
    for (MenuOpen of sideMenuOpen){
        const sideMenu = document.querySelector(MenuOpen.getAttribute('href'));
        
        MenuOpen.addEventListener('click', function (event) {
            sideMenu.classList.add('open');
            event.preventDefault();
        });
    }
}


const sideMenuClose = document.querySelectorAll('.js-side-menu-close');

if (sideMenuClose.length > 0){
    for (MenuClose of sideMenuClose){
        const sideMenu = document.querySelector(MenuClose.getAttribute('href'));
        
        MenuClose.addEventListener('click', function (event) {
            sideMenu.classList.remove('open');
            event.preventDefault();
        });
    }
}
