-- Step 1: Creating DataBase
CREATE DATABASE IF NOT EXISTS NetflixDB;
SHOW DATABASES LIKE 'NetflixDB';

-- Step 2: Using DB
USE NetflixDB;

-- Step 3: Creating Tables - Users, Movies, WatchHistory & Reviews
-- Step 3a: Creating Users Table

CREATE TABLE Users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    registration_date DATE NOT NULL,
    plan ENUM('Basic', 'Standard', 'Premium') DEFAULT 'Basic'
);
    
-- Step 3b: Creating Movies Table
CREATE TABLE Movies (
	movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    release_year YEAR NOT NULL,
    rating DECIMAL(3, 1) NOT NULL
);
    
-- Step 3c: Creating WatchHistory Table 
CREATE TABLE WatchHistory (
    watch_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    movie_id INT,
    watched_date DATE NOT NULL,
    completion_percentage INT CHECK (completion_percentage >= 0 AND completion_percentage <= 100),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);
    
-- Step 3d: Creating Reviews Table 
CREATE TABLE Reviews (
	review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    review_text TEXT,
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5),
    review_date DATE NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
    
-- Step 4: Loading the Values into the Tables
-- Step 4a: Loading Users Table Values

INSERT INTO Users (name, email, registration_date, plan) 
VALUES
('John Doe', 'john.doe@example.com', '2024-01-10', 'Premium'),
('Jane Smith', 'jane.smith@example.com', '2024-01-15', 'Standard'),
('Alice Johnson', 'alice.johnson@example.com', '2024-02-01', 'Basic'),
('Bob Brown', 'bob.brown@example.com', '2024-02-20', 'Premium');
Select * FROM Users;

-- Step 4b: Loading Movies Table Values
 INSERT INTO Movies (title, genre, release_year, rating) VALUES
('Stranger Things', 'Drama', 2016, 8.7),
('Breaking Bad', 'Crime', 2008, 9.5),
('The Crown', 'History', 2016, 8.6),
('The Witcher', 'Fantasy', 2019, 8.2),
('Black Mirror', 'Sci-Fi', 2011, 8.8);
Select * FROM Movies;

-- Step 4c: Loading WatchHistory Table Values
INSERT INTO WatchHistory (user_id, movie_id, watched_date, completion_percentage) 
VALUES
(1, 1, '2024-02-05', 100),
(2, 2, '2024-02-06', 80),
(3, 3, '2024-02-10', 50),
(4, 4, '2024-02-15', 100),
(1, 5, '2024-02-18', 90);
Select * FROM WatchHistory;

-- Step 4d: Loading Reviews Table Values
INSERT INTO Reviews (movie_id, user_id, review_text, rating, review_date) 
VALUES
(1, 1, 'Amazing storyline and great characters!', 4.5, '2024-02-07'),
(2, 2, 'Intense and thrilling!', 5.0, '2024-02-08'),
(3, 3, 'Good show, but slow at times.', 3.5, '2024-02-12'),
(4, 4, 'Fantastic visuals and acting.', 4.8, '2024-02-16');
Select * FROM Reviews;