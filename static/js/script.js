$.ajax({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/csrf/',
    success: (data) => {
        getData()
    }
})

let csrf = ''
const getData = () => {
    const cookie = document.cookie.split(';')
    for (let i = 0; i < cookie.length; i++) {
        if (cookie[i].split('=')[0] === 'csrftoken') {
            csrf = document.cookie.split('=')[i + 1];
        };
    }
}

const base_url = 'http://127.0.0.1:8000/api/v1/';
function onLoad() {
    div_main = document.getElementById('container');
    const add = document.getElementById("add");
    add.addEventListener('click', calculate_this);
    const subsrtact = document.getElementById("subsrtact");
    subsrtact.addEventListener('click', calculate_this);
    let divide = document.getElementById("divide");
    divide.addEventListener('click', calculate_this);
    let multiply = document.getElementById("multiply");
    multiply.addEventListener('click', calculate_this);
    const a = document.getElementById("a");
    const b = document.getElementById("b");
}
window.addEventListener('load', onLoad);


const calculate_this = function () {

    try {
        let url = base_url + this.id + '/';
        let data = $.ajax({
            method: 'POST',
            data: JSON.stringify({ 'a': a.value, 'b': b.value }),
            headers: {
                'X-CSRFToken': csrf
            },
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            url: url,
            success: (data) => {
                render(data);
            },
            error: (data) => {
                render_error(data);
            }
        });
        return
    } catch (response) {
    }
}

function render(data) {
    div_main = document.getElementById('container');
    if (div_card = document.getElementById('answer')) {
        div_card.remove();
    };
    let div = document.createElement('div');
    div.className = "alert alert-success";
    div.id = 'answer'
    div.innerHTML = '<div class="card-body" id="post"> <h3> Ответ</h3><p class="card-text"> ' + data.answer + '</p>';
    div_main.append(div);
}

function render_error(data) {
    div_main = document.getElementById('container');
    if (div_card = document.getElementById('answer')) {
        div_card.remove();
    };
    let div = document.createElement('div');
    div.className = "alert alert-danger";
    div.id = 'answer'
    div.innerHTML = '<div class="card-body" id="post"> <h3> Ответ</h3><p class="card-text"> ' + data.responseJSON.error + '</p>';
    div_main.append(div);
}
