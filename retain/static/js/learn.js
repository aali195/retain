function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var url = '/api/v1/user/progress/learn/';
var id;
var note;


$(document).ready(function() {
    $.ajax({
        type:'GET',
        url: url,
        headers: {
            "X-CSRFToken": csrftoken
        },
        dataType: 'json',  
        success: function (data) {  
            $('#statement').html(data[0].statement);
            $("#image").attr("src",data[0].image);
            id = data[0].id;
        },
        error: function(data) {
            console.log(data);
        },
    });
});


$('#next').on('click', function() {
    var jsonData;

    if ($('#note').val().trim() != '') {
        note = $('#note').val();
        jsonData = {
            'statement_id': id,
            'note': note
        }
    } else {
        jsonData = {
            'statement_id': id
        }
    }

    $.ajax({
        type:'POST',
        url: url,
        headers: {
            "X-CSRFToken": csrftoken
        },
        contentType: "application/json",
        data: JSON.stringify(jsonData),
        success: function(data) {
            if (('#completed-count') != ('#collection-size')) {
                location.reload();
            } else {
                window.location.href = "/users/dashboard";
            }
        },
        failure: function(err) {
            console.log(err);
        },
    });
});