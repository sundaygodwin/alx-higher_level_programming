// Make a GET request to the URL using jQuery's $.ajax() function
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(response) {
        // Extract the character name from the response
        var characterName = response.name;
        
        // Update the text content of the #character
        $('#character').text(characterName);
    },
    error: function(xhr, status, error) {
        // Handle any errors that occur during the request
        console.error('Error fetching character name:', error);
    }
});
