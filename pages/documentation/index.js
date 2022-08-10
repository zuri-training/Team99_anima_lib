const hamburger = document.querySelector('.header .mobile__navbar .hamburger');
const mobile_menu = document.querySelector('.header .mobile__navbar ul');
const menu_item = document.querySelectorAll('.header .mobile__navbar ul li a');
const header = document.querySelector('.header.container');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    mobile_menu.classList.toggle('active');
});

document.addEventListener("scroll", ()=> {
    var scroll_position = window.scrollY;
    if(scroll_position > 250){
        header.style.backgroundColor = '#29323c';
    }else{
        header.style.backgroundColor = "transparent"
    }
})

menu_item.forEach(item=> {
    item.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    });
});

