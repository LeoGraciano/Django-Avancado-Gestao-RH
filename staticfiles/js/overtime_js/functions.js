function userOverTime(pk,params=null) {
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        type: 'POST',
        url: `/overtime/user-overtime/${pk}`,
        data: {
            csrfmiddlewaretoken: token,
            'params_recovery': params
        },
        success: function (response) {
            console.log('Sucesso!!!')
            var message = document.getElementById('message')
            if (response['message']) {
                message.innerHTML = response['message'] +'<br>'
            };
            if (response['bank_hours']) {
                message.innerHTML += response['bank_hours']
            }
        }
    })

}
