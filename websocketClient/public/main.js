//main.js
$(document).on('submit', '#form', function(e){
    e.preventDefault();
    var input = document.getElementById('input').value;
    Submit(input);
    console.log(input);
});

function Submit(input) {
    $.ajax({
        type:'POST',
        url:'/search',
        processData: false,
        contentType: "application/json; charset=utf-8",
        async: true,
        cache: false,
        data : JSON.stringify({search:input}),
        success: function(response){
            console.log(response);
        }
    });
}
