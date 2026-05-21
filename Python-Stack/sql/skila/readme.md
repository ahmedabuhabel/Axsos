# Sakila Database Queries Solution

This repository contains SQL solutions for querying the **Sakila DVD Rental Database**. The exercises focus heavily on multi-table relational joins (`INNER JOIN`), conditional filtering across combined datasets (`WHERE`, `IN`, `LIKE`), and string manipulation functions (`CONCAT`).

## Prerequisites

To run these queries, ensure you have:

1. **MySQL Server** installed.
2. The **Sakila Database** schema and data populated.
3. **MySQL Workbench** or any other compatible SQL terminal interface.

---

## Queries and Implementations

### Q1: Customers in City Address Area

Retrieves user information for customers tied specifically to address record ID 312.

```sql
SELECT c.first_name, c.last_name, c.email, address.address_id
FROM customer AS c
     JOIN address ON c.address_id = address.address_id
WHERE c.address_id = 312;

```

### Q2: Comedy Film Selection

Extracts comprehensive movie catalog details specifically categorized under the 'Comedy' genre.

```sql
SELECT f.title, f.description, f.release_year, f.rating, f.special_features, category.name AS CategoryName
FROM film AS f
     JOIN film_category ON f.film_id = film_category.film_id
     JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';

```

### Q3: Actor Filmography (Actor ID: 5)

Compiles a complete list of films featuring the actor with an ID of 5, stringing their first and last names together.

```sql
SELECT CONCAT(a.first_name, ' ', a.last_name) AS Name, f.title, f.description, f.release_year
FROM actor AS a
     JOIN film_actor ON a.actor_id = film_actor.actor_id
     JOIN film AS f ON f.film_id = film_actor.film_id
WHERE a.actor_id = 5;

```

### Q4: Store 1 Customers in Targeted Cities

Targets specific customer segments belonging to Store 1 who reside within city IDs: 1, 42, 312, or 459.

```sql
SELECT c.first_name, c.last_name, c.email, a.address
FROM customer AS c
     JOIN address AS a ON c.address_id = a.address_id
WHERE c.store_id = 1
  AND a.city_id IN (1, 42, 312, 459);

```

### Q5: G-Rated Behind the Scenes Movies (Actor ID: 15)

Filters down movies starring actor ID 15 that are rated 'G' and explicitly feature 'Behind the Scenes' footage.

```sql
SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM film AS f
     JOIN film_actor AS fa ON f.film_id = fa.film_id
WHERE fa.actor_id = 15
  AND f.rating = 'G'
  AND f.special_features LIKE '%behind the scenes%';

```

### Q6: Complete Cast List for Film 369

Returns the movie title along with the identification records and combined names of all actors cast in film ID 369.

```sql
SELECT f.film_id, f.title, a.actor_id, CONCAT(a.first_name, ' ', a.last_name) AS Name
FROM film AS f
     JOIN film_actor ON f.film_id = film_actor.film_id
     JOIN actor AS a ON film_actor.actor_id = a.actor_id
WHERE f.film_id = 369;

```

### Q7: Drama Movie Rental Catalog Deals

Extracts all films belonging to the 'Drama' genre that maintain a standard rental pricing tier of $2.99.

```sql
SELECT f.title, f.description, f.release_year, f.rating, f.special_features, category.name AS Genre
FROM film AS f
     JOIN film_category AS fc ON f.film_id = fc.film_id
     JOIN category ON category.category_id = fc.category_id
WHERE f.rental_rate = 2.99
  AND category.name = 'Drama';

```

### Q8: Action Catalog Features Starring Sandra Kilmer

Performs a comprehensive four-table join to retrieve all 'Action' movies starring the specific actor 'Sandra Kilmer'.

```sql
SELECT f.title, f.description, f.release_year, f.rating, f.special_features, category.name AS Genre, a.first_name, a.last_name
FROM film AS f
     JOIN film_category AS fc ON f.film_id = fc.film_id
     JOIN category ON category.category_id = fc.category_id
     JOIN film_actor ON f.film_id = film_actor.film_id
     JOIN actor AS a ON film_actor.actor_id = a.actor_id
WHERE a.first_name = 'SANDRA'
  AND a.last_name = 'KILMER';

```

---

## Relational Operations Demonstrated

- **Many-to-Many Join Resolution:** Resolves many-to-many physical database linkages via junction schemas like `film_actor` and `film_category`.
- **String Concatenation:** Implements `CONCAT(string1, string2)` formatting directly at the query projection tier to output cleanly combined dataset names.
- **Wildcard Matching:** Uses the `LIKE '%...%'` operator combined with percentage match expressions to run substring lookups on multi-valued text fields.

```

```
