// Make a GET request to the URL using jQuery's $.ajax() function
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(response) {
        // Select the #list_movies
        var list = $('#list_movies');
        
        // Iterate over the results
        response.results.forEach(function(movie) {
            // Extract the title of each movie
            var title = movie.title;
            
            // Create a new <li> with the movie title
            var listItem = $('<li>').text(title);
            
            // Append the listItem to #list_movies
            list.append(listItem);
        });
    },
    error: function(xhr, status, error) {
        // Handle any errors that occur during the request
        console.error('Error fetching movies:', error);
    }
});
