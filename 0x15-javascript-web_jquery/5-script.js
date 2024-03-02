// Add a click event handler to the DIV#add_item element
$('#add_item').click(function() {
    // Create a new <li> element with the text "Item"
    var newItem = $('<li>Item</li>');
    
    // Append newItem to the <ul class="my_list">
    $('ul.my_list').append(newItem);
});
