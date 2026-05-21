-- Q1: Insert Users and their Friendships
INSERT INTO users (first_name, last_name)
VALUES ('Amy', 'Giver'),
    ('Eli', 'Byers'),
    ('Big', 'Bird'),
    ('Kermit', 'The Frog'),
    ('Marky', 'Mark');
-- Q2: Query Friendships
SELECT users.first_name,
    users.last_name,
    user2.first_name as friend_first_name,
    user2.last_name friend_last_name
FROM users
    JOIN friendships ON users.id = friendships.user_id
    LEFT JOIN users as user2 ON friendships.friend_id = user2.id