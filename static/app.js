$(document).ready(function(){
    $('.randomize-button').on('click', function(e){
        e.preventDefault();
        var buttonNum = $(this).attr('num');
        req = $.ajax({
            url: '/random_process',
            type: 'POST',
            data: {id : buttonNum}
        });
        req.done(function(data){
            $('#randomize'+buttonNum).val(data.random_word)
            if ($('#randomize'+buttonNum).val()){
                $('#randomize'+buttonNum).val(data.random_word)
            }
        });
    });
});