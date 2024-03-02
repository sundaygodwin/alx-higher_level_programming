$(document).ready(function() {
    $('#btn_translate').click(function() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Fetch the translation from the API
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
            // Update the text of the <div> with the translation
            $('#hello').text(data.hello);
        });
    });
});
