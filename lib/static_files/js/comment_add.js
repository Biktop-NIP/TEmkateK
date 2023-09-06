function comment(url){
    const commentInput = document.querySelector('#id_text');
    fetch(url+`?text=${commentInput.value}`).then(response => {
        if (response.ok){
            const comments = document.querySelector('.comments');
            comments.innerHTML = `<div class="comment"><div><p class="comment_user-name">You</p><p class="comment__text">${commentInput.value}</p><div class="comment-score"></div></div></div>` + comments.innerHTML  
        }
    })
}
