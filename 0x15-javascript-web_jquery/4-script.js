// Add a click event handler to the DIV#toggle_header element
$('#toggle_header').click(function() {
    // Select the <header> element
    var header = $('header');
    	// Check if the header has class "red"
    if (header.hasClass('red')) {
        // If it has class "red", remove "red" and add "green"
        header.removeClass('red').addClass('green');
    } else {
        // If it doesn't have class "red" (i.e., it has class "green"),
	// remove "green" and add "red"
        header.removeClass('green').addClass('red');
    }
});
