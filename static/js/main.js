var answer;

$(document).ready(function () {
    get_new_quiz()
});

$(document).on('submit', '#capital_quiz_form', function (e) {
    e.preventDefault();
    console.log($('#answer').val())
    if (answer.toUpperCase() == $('#answer').val().toUpperCase()) {
        Swal.fire(
            "Correct",
            "Well done!",
            "success"
        ).then(function () {
            get_new_quiz();
            document.form.reset()
        });
    } else {
        Swal.fire(
            "Incorrect",
            "The Answer is " + answer,
            "error"
        ).then(function () {
            get_new_quiz();
            document.form.reset()
        });
    }
})

function get_new_quiz() {
    $.ajax({
        type: 'GET',
        url: '/capital-quiz/get-quiz',
        success: function (data) {
            document.getElementById("question").innerText = "Question: What is the capital city of  " + data.country;
            answer = data.capital;
        }
    })
}
