# Friendships Database Queries Solution

This repository contains SQL solutions for querying a self-referencing relationship schema inside a **Friendships Database**. The primary focus of this exercise is implementing a **Self-Join** operation, allowing a single table (`users`) to establish many-to-many relationship connections to itself via a junction table (`friendships`).

## Prerequisites

To run these queries, ensure you have:

1. **MySQL Server** installed and running.
2. The `friendships_schema` forward-engineered and active.
3. **MySQL Workbench** or an equivalent SQL client interface.

---

## Database Architecture Overview

To map a many-to-many relationship where users can be friends with other users, the schema employs two main tables:

1. `users`: Stores core profile rows (e.g., `id`, `first_name`, `last_name`).
2. `friendships`: A bridge/junction table containing foreign keys mapping back to the users table (`user_id` and `friend_id`).

---

## Queries and Implementations

### Q1: Seeding Users Data

Inserts core profile rows into the database to establish a baseline group of individuals.

```sql
INSERT INTO users (first_name, last_name) VALUES
('Amy', 'Giver'),
('Eli', 'Byers'),
('Big', 'Bird'),
('Kermit', 'The Frog'),
('Marky', 'Mark');

```

### Q2: Querying Friendships (The Self-Join)

Combines rows from the `users` table twice using the `friendships` junction table. This maps each user side-by-side with their corresponding friends while utilizing column aliasing (`AS`) to keep the resulting output clean and distinguishable.

```sql
SELECT users.first_name,
       users.last_name,
       user2.first_name AS friend_first_name,
       user2.last_name AS friend_last_name
FROM users
     JOIN friendships ON users.id = friendships.user_id
     LEFT JOIN users AS user2 ON friendships.friend_id = user2.id;

```

---

## Relational Operations Demonstrated

- **Table Aliasing (`AS user2`):** Because the query links the `users` table twice, assigning a temporary name/alias (`user2`) allows the SQL engine to distinguish between the person initiating the friendship and the person receiving it.
- **Junction Table Traversal:** Demonstrates how data flows from `users.id` ➡️ `friendships.user_id`, then bridges across from `friendships.friend_id` ➡️ `user2.id`.
- **Column Renaming:** Uses aliases (`friend_first_name`, `friend_last_name`) on the projected fields so the final grid output avoids conflicting column naming issues.

```

```
