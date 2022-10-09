SELECT movies.title FROM movies WHERE id IN (
    SELECT movie_id FROM stars 
    JOIN people ON stars.person_id = people.id 
    WHERE name IN (
        "Helena Bonham Carter", "Johnny Depp"
        )
    GROUP BY movie_id 
    HAVING COUNT(person_id) = 2
    );