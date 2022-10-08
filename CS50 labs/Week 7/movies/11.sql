SELECT movies.title FROM movies, stars, people, ratings WHERE people.id = stars.person_id AND stars.movie_id = movies.id AND people.name = "Chadwick Boseman" ORDER BY ratings.rating DESC LIMIT 5;