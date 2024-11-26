-- 1 --
SELECT title FROM movies WHERE year = '2008';

-- 2 --

SELECT birth FROM people WHERE name = 'Emma Stone';

-- 3 --

SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC;

-- 4 --

SELECT COUNT(movie_id) FROM ratings WHERE rating = 10;

-- 5 --

SELECT title, year FROM movies
WHERE title LIKE 'Harry Potter%'
ORDER BY year ASC;

-- 6 --

SELECT AVG(rating) FROM movies, ratings WHERE movies.id = ratings.movie_id AND movies.year = 2012;

-- 7 --

SELECT title, rating FROM movies, ratings WHERE movies.id = ratings.movie_id AND movies.year = 2010 ORDER BY rating DESC, title ASC;

-- 8 --

SELECT name FROM people, stars, movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id AND movies.title = 'Toy Story';

-- 9 --

SELECT DISTINCT people.name FROM people, stars, movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id AND movies.year = 2004 ORDER BY people.birth;

-- 10 --

SELECT name FROM people
WHERE id IN (
    SELECT person_id FROM movies
    JOIN directors ON movies.id = directors.movie_id
    JOIN ratings ON directors.movie_id = ratings.movie_id
    WHERE rating >= 9.0
    );

-- 11 --

SELECT title FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE id IN (
    SELECT movie_id FROM stars
    JOIN people ON stars.person_id = people.id
    WHERE name = 'Chadwick Boseman'
    )
ORDER BY rating DESC LIMIT 5;

-- 12 --

SELECT movies.title FROM movies WHERE id IN (
    SELECT movie_id FROM stars
    JOIN people ON stars.person_id = people.id
    WHERE name IN (
        "Helena Bonham Carter", "Johnny Depp"
        )
    GROUP BY movie_id
    HAVING COUNT(person_id) = 2
    );

-- 13 --

SELECT people.name FROM people WHERE id IN (
    SELECT person_id FROM stars WHERE movie_id IN (
        SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id
        WHERE name = 'Kevin Bacon' AND birth = 1958
    )
)
AND NOT name = 'Kevin Bacon';


