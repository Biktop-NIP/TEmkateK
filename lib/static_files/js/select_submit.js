const body = document.querySelector('body')
const selects = document.querySelectorAll('.select');

const urlSearchParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlSearchParams.entries());

/*if ('genres' in params){
    genres_input = document.querySelector('input[name="genres"]');
    genres_input.value = genres
}*/

selects.forEach(element => {
    button = element.querySelector('.select__dropdown__button');
    input = element.querySelector('.select__input');
    form = document.forms[0]

    if (input.name in params){
        input.value = params[input.name];
        element.querySelectorAll('.select__dropdown__list-item').forEach(el => {
            if (el.dataset.value == params[input.name]){
                button.innerText = el.innerHTML;
            }
        })
    }


    button.addEventListener('click', (event) => {
        event.preventDefault();
        element.classList.toggle('open');
    });

    body.addEventListener('click', (event) => {
        if ( event.target.classList.contains('select__dropdown__list-item') ){
            button.innerText = event.target.innerText;
            input.value = event.target.dataset.value
            element.classList.remove('open');
            form.submit()
            
        }
        else if ( !event.target.classList.contains('select__dropdown__button')) {
            element.classList.remove('open');
        }
        
    })
});
