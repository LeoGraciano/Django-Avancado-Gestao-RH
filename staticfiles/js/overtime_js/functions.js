function userOverTime(pk) {
    console.log(pk)
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: `/overtime/user-overtime/${pk}`,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (result) {
            console.log('Sucesso!!!')
            if (result['message']) {
                $("#message").text(result['message'])
            };
        }
    })

}
