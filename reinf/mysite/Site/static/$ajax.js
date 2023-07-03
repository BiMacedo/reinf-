$.ajax({
  URL: '/user_login',
  method: 'POST',
  Headers:{
    'X-CSRFToken': getCookie('csrftoken')
  }
});