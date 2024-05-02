$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(films) {
        for (const film of films.results) {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        }
    }
});
