-- Q1: Customer Information with Address
select c.first_name,
    c.last_name,
    c.email,
    address.address_id
from customer as c
    join address on c.address_id = address.address_id
where c.address_id = 312;
-- Q2: Film Information by Category
select f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features,
    category.name as CategoryName
from film as f
    join film_category on f.film_id = film_category.film_id
    join category on category.category_id = film_category.category_id
where category.name = 'Comedy';
-- Q3: Actor Information with Film Details
select concat(a.first_name, ' ', a.last_name) as Name,
    f.title,
    f.description,
    f.release_year
from actor as a
    join film_actor on a.actor_id = film_actor.actor_id
    join film as f on f.film_id = film_actor.film_id
where a.actor_id = 5;
-- Q4: Customer Information with Address
select c.first_name,
    c.last_name,
    c.email,
    a.address
from customer as c
    join address as a on c.address_id = a.address_id
where c.store_id = 1
    and a.city_id in (1, 42, 312, 459);
-- Q5: Film Information by Actor and Rating
select f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features
from film as f
    join film_actor as fa on f.film_id = fa.film_id
where fa.actor_id = 15
    and f.rating = 'G'
    and f.special_features like '%behind the scenes%';
-- Q6: Film Information by Film ID
select f.film_id,
    f.title,
    a.actor_id,
    concat(a.first_name, ' ', a.last_name) as Name
from film as f
    join film_actor on f.film_id = film_actor.film_id
    join actor as a on film_actor.actor_id = a.actor_id
where f.film_id = 369;
-- Q7: Film Information by Rental Rate and Category
select f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features,
    category.name as Genre
from film as f
    join film_category as fc on f.film_id = fc.film_id
    join category on category.category_id = fc.category_id
where f.rental_rate = 2.99
    and category.name = 'Drama';
-- Q8: Film Information by Actor Name
select f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features,
    category.name as Genre,
    a.first_name,
    a.last_name
from film as f
    join film_category as fc on f.film_id = fc.film_id
    join category on category.category_id = fc.category_id
    join film_actor on f.film_id = film_actor.film_id
    join actor as a on film_actor.actor_id = a.actor_id
where a.first_name = 'SANDRA'
    and a.last_name = 'KILMER'