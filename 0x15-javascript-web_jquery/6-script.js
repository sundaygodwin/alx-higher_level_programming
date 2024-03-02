// add a click event handler to the DIV#update_header element
$('#update_header').click(function() {
    // Select the <header> element
    var header = $('header');
    
    // Update the text content of <header> to "New Header!!!"
    header.text('New Header!!!');
});
