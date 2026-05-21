--Q1: Slovene Speakers
select countries.name,
    languages.language,
    languages.percentage
from countries
    join languages on countries.id = languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;
--Q2: Number of Cities per Country
select countries.name,
    count(cities.name) as TotalNumberOfCities
from countries
    join cities on countries.id = cities.country_id
group by countries.name
order by TotalNumberOfCities desc;
--Q3: Cities in Mexico
select cities.name,
    cities.population,
    cities.country_id
from cities
    join countries on countries.id = cities.country_id
where countries.name = 'Mexico'
    and cities.population > 500000
order by cities.population desc;
--Q4: Languages with High Percentage
select countries.name,
    languages.language,
    languages.percentage
from countries
    join languages on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;
--Q5: Countries with Small Surface Area and Large Population
select countries.name,
    countries.surface_area,
    countries.population
from countries
where surface_area < 501
    and population > 100000;
--Q6: Countries with High GDP per Capita
select c.name,
    c.government_form,
    c.capital,
    c.life_expectancy
from countries as c
where c.government_form = 'Constitutional Monarchy'
    and c.capital > 200
    and c.life_expectancy > 75;
--Q7: Cities in Argentina
select c.name as country_name,
    ci.name as city_name,
    ci.district,
    ci.population
from countries as c
    join cities as ci on c.id = ci.country_id
where c.name = 'Argentina'
    and ci.district = 'Buenos Aires'
    and ci.population > 500000;
--Q8: Number of Countries per Region
select region,
    count(countries.name) as countries
from countries
group by countries.region
order by countries desc write readme file in md format