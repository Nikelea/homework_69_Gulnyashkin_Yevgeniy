$.ajax({   method:'get',
url: 'http://127.0.0.1:8000/api/v1/csrf/',
success: (data)=>{
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
