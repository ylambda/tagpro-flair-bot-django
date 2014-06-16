var csrftoken = $.cookie('csrftoken');
var $radios = $('#flair-form input[name="flair"]');
var currentFlair;

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function handleNetworkError(){
    console.log("The request failed. Try again.");
}

function setCurrentFlair(){
    currentFlair = $radios.filter(":checked").val();
}

function selectFlairByValue(value){
    var valElement = $('#flair-form input[name=flair][value='+value+']');
    $radios.filter(":checked").attr("checked", false);
    valElement.prop("checked", true);
    setCurrentFlair();
}

$(function(){
    $('#flair-form input[type="submit"]').hide();
    setCurrentFlair();
    $radios.click(function(e){
        e.preventDefault();
        $radios.attr("disabled", true);
        var selectedFlair = $(this).val();
        $.post(
            '/set_flair/',
            {'flair': selectedFlair},
            function(data, success, xhr){
                $radios.attr("disabled", false);
                if(success){
                    if(data['success']){
                        selectFlairByValue(selectedFlair);
                        return;
                    }else{
                        console.log("Error", data['error']);
                    }
                }else{
                    handleNetworkError();
                }
                selectFlairByValue(currentFlair);

            }
        );
    });
});
