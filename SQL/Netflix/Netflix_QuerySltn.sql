-- Question 1. List all users subscribed to the Premium plan

SELECT U.name AS User_Name, U.Plan AS Plan_Subscribed
FROM Users U
WHERE Plan = 'Premium';

-- Question 2. Retrieve all movies in the Drama genre with a rating higher than 8.5

SELECT M.title AS Movie_Title, M.Rating
FROM Movies M
WHERE genre = 'Drama' AND rating > 8.5;

-- Question 3. Find the average rating of all movies released after 2015

SELECT M.title AS Movie_Title, M.rating AS Individual_Movie_Rating, AVG(M.rating) OVER () AS Avg_Rating_After_2015
FROM Movies M
WHERE M.release_year > 2015;

-- Question 4. List the names of users who have watched the movie Stranger Things along with their completion percentage

SELECT U.name AS User_name, W.completion_percentage AS Movie_Completion_Percentage
FROM Users U
JOIN WatchHistory W ON U.user_id = W.user_id
JOIN Movies M ON W.movie_id = M.movie_id
WHERE  title = 'Stranger Things';

-- Question 5. Find the name of the user(s) who rated a movie the highest among all reviews

SELECT U. name AS User_Name, R.rating as Highest_Review_Rate
FROM Users U 
JOIN Reviews R ON U. User_id = R. User_id
ORDER BY R.rating DESC
LIMIT 1;

-- Question 6. Calculate the number of movies watched by each user and sort by the highest count.

SELECT U.name AS User_Name, COUNT(W.watch_id) AS Num_Of_Movies_Watched
FROM Users U
JOIN WatchHistory W ON U.user_id = W. user_id
GROUP BY U.User_id
ORDER BY Num_Of_Movies_Watched DESC;

-- Question 7. List all movies watched by John Doe, including their genre, rating, and his completion percentage

SELECT M.title AS Movie_Title, M.Genre, M.Rating, W. completion_percentage AS Movie_Completion_Percentage
FROM Movies M
JOIN WatchHistory W ON M.Movie_id = W.Movie_id
JOIN Users U ON W. User_id = U.User_id
WHERE U.name = 'John Doe';

-- Question 8. Update the movie's rating for Stranger Things by 9

UPDATE Movies
SET rating = 8.7
WHERE title = 'Stranger Things';

-- Storing Original Rating
SET @old_rating := (SELECT rating FROM Movies WHERE title = 'Stranger Things');

-- Updating Rating
UPDATE Movies
SET rating = 9
WHERE title = 'Stranger Things';

-- Showing Both Old & New Rating
SELECT M.title as Movie_Title, @old_rating AS Original_Rating,  M.rating AS Updated_Rating
FROM Movies M
WHERE title = 'Stranger Things';

-- Question 9. Remove all reviews for movies with a rating below 4.0

START TRANSACTION;

-- Step 1: Saving BEFORE snapshot into a temporary table
DROP TEMPORARY TABLE IF EXISTS Reviews_Before;
CREATE TEMPORARY TABLE Reviews_Before AS
SELECT R.movie_id, R.rating, M.title
FROM Reviews R
JOIN Movies M ON R.movie_id = M.movie_id;

-- Step 2: Deleting reviews with rating < 4.0
DELETE FROM Reviews
WHERE rating < 4.0;

-- Step 3: Combining BEFORE and AFTER in one result
SELECT 'BEFORE' AS version, movie_id, rating, title
FROM Reviews_Before
UNION ALL
SELECT 'AFTER' AS version, R.movie_id, R.rating, M.title
FROM Reviews R
JOIN Movies M ON R.movie_id = M.movie_id;
-- Commiting to finalize
COMMIT;

-- Rollbacking to revert changes

START TRANSACTION;
DELETE FROM Reviews WHERE rating < 4.0;
ROLLBACK;

-- Question 10. Fetch all users who have reviewed a movie but have not watched it completely (completion percentage < 100)

SELECT DISTINCT  U.Name AS User_Name, M.title AS Movie_Title, R.Review_Text, W.Completion_Percentage
FROM Users U 
JOIN Reviews R ON U.user_id = R.user_id
JOIN Movies M ON R.movie_id = M.movie_id
JOIN WatchHistory W ON R.user_id = W.user_id AND R.movie_id = W.movie_id
WHERE W.Completion_Percentage < 100;

-- Question 12. Retrieve all users who have reviewed the movie Stranger Things, including their review text and rating

SELECT U.Name, R.Review_Text, R.Rating
FROM Users U 
JOIN Reviews R ON U.user_id = R.user_id
JOIN Movies M ON R.movie_id = M.movie_id
WHERE M.title = 'Stranger Things';

-- Question 13. Fetch the watch history of all users, including their name, email, movie title, genre, watched date and completion percentage

SELECT U.Name, U.Email, M.Title AS Movie_Title, M.Genre, W.Watched_Date, W.Completion_Percentage
From Users U 
JOIN WatchHistory W ON U.user_id = W.user_id
JOIN Movies M ON W.movie_id = M.movie_id;

-- Question 14. List all movies along with the total number of reviews and average rating for each movie including only movies with at least two reviews

SELECT M.Title AS Movie_Title, COUNT(R.Review_Id) AS Total_Numb_Of_Reviews, AVG(R.Rating) AS AVG_Rating
FROM Movies M
JOIN Reviews R ON M.movie_id = R. movie_id
GROUP BY M.Title
HAVING Total_Numb_Of_Reviews >= 2;




