const body = document.querySelector('body')
const selects = document.querySelectorAll('.select');

const urlSearchParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlSearchParams.entries());

selects.forEach(element => {
    button = element.querySelector('.select__dropdown__button');
    input = element.querySelector('.select__input');

    
    button.addEventListener('click', (event) => {
        event.preventDefault();
        element.classList.toggle('open');
    });


    body.addEventListener('click', (event) => {
        if ( event.target.classList.contains('select__dropdown__list-item') ){
            button.innerText = event.target.innerText;
            input.value = event.target.dataset.value
            element.classList.remove('open');
            
        }
        else if ( !event.target.classList.contains('select__dropdown__button')) {
            element.classList.remove('open');
        }
        
    })
});
