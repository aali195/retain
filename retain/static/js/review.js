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

var url = '/api/v1/user/progress/review/';

var id;
var correctAns;
var is_correct;

$(document).ready(function() {
    $.ajax({
        type:'GET',
        url: url,
        headers: {
            'X-CSRFToken': csrftoken
        },
        dataType: 'json',  
        success: function (data) {  
            id = data.statement_id;
            correctAns = data.answer;
            $('#question').html('Q: ' + data.question);
            setAnswers(data);
            setDetails(data);
        },
        error: function(err) {
            console.log(err);
        },
    });
    
});

setAnswers = function(data) {

    var answersArray = new Array();
    answersArray[0] = data.wrong_answer_1;
    answersArray[1] = data.wrong_answer_2;
    answersArray[2] = data.wrong_answer_3;
    answersArray[3] = correctAns;

    shuffleArray(answersArray);

    var ans1 = answersArray.pop();
    var ans2 = answersArray.pop();
    var ans3 = answersArray.pop();
    var ans4 = answersArray.pop();

    $('#ans1').text(ans1);
    $('input:radio[name=r-ans1]').val(ans1);
    $('#ans2').text(ans2);
    $('input:radio[name=r-ans2]').val(ans2);
    $('#ans3').text(ans3);
    $('input:radio[name=r-ans3]').val(ans3);
    $('#ans4').text(ans4);
    $('input:radio[name=r-ans4]').val(ans4);
    $('#quiz').fadeIn(1000);
};

function shuffleArray(array) {
    var c = array.length, t, r;
    while (0 !== c) {
        r = Math.floor(Math.random() * c);
        c -= 1;
        t = array[c];
        array[c] = array[r];
        array[r] = t;
    }
    return array;
}

setDetails = function(data) {
    $('#image').attr('src',data.image);
    $('#statement').html(data.statement);
    $('#note').html(data.note);
};

$('label.btn').on('click',function () {
    var choice = $(this).find('input:radio').val();
    $('#quiz').fadeOut();
    checkAns(choice);

    var jsonData = {
        'statement_id': id,
        'is_correct': is_correct
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
            $('#quiz').fadeOut();
            checkAns(choice);
            $('#statement-details').fadeIn();
            $('#next').show();
        },
        failure: function(err) {
            console.log(err);
        },
    });
});

checkAns = function(choice) {
    if (choice != correctAns) {
        is_correct = false;
        $('#question').html('INCORRECT');
    } else {
        is_correct = true;
        $('#question').html('CORRECT');
    }
};

$('#next').on('click',function () {
    location.reload();
});