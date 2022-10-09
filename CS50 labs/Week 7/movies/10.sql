SELECT name FROM people
WHERE id IN (
    SELECT person_id FROM movies 
    JOIN directors ON movies.id = directors.movie_id 
    JOIN ratings ON directors.movie_id = ratings.movie_id
    WHERE rating >= 9.0
    );