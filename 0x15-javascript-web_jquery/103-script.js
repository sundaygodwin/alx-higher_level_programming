$(document).ready(function() {
    // Function to fetch translation when the user clicks Translate button or presses Enter
    function fetchTranslation() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Fetch the translation from the API
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
            // Update the text of the <div> with the translation
            $('#hello').text(data.hello);
        });
    }

    // Fetch translation when the user clicks Translate button
    $('#btn_translate').click(fetchTranslation);

    // Fetch translation when the user presses Enter in the language code input field
    $('#language_code').keypress(function(event) {
        // Check if the Enter key (key code 13) is pressed
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
