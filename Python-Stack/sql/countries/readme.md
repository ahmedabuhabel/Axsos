# World Database Queries Solution

This repository contains a collection of SQL queries executed on the **World Database**. The queries cover essential relational database concepts including `JOIN` operations, conditional filtering (`WHERE`), data aggregation (`GROUP BY`, `COUNT`), and result sorting (`ORDER BY`).

## Prerequisites

To run these queries, you need to have:

1. **MySQL Server** installed and running.
2. The **World Database** schema and data imported.
3. A database client like **MySQL Workbench** or the command-line interface.

---

## Queries and Implementations

### Q1: Slovene-Speaking Countries

Retrieves all countries where Slovene is spoken, along with the official language name and its spoken percentage. Results are sorted by percentage in descending order.

```sql
SELECT countries.name,
       languages.language,
       languages.percentage
FROM countries
     JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

```

### Q2: Number of Cities per Country

Aggregates the total number of cities located within each country. The results are ordered from the country with the highest number of cities to the lowest.

```sql
SELECT countries.name,
       COUNT(cities.name) AS TotalNumberOfCities
FROM countries
     JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY TotalNumberOfCities DESC;

```

### Q3: Major Cities in Mexico

Finds all cities in Mexico that have a population strictly greater than 500,000. The output is organized by population density from highest to lowest.

```sql
SELECT cities.name,
       cities.population,
       cities.country_id
FROM cities
     JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'
  AND cities.population > 500000
ORDER BY cities.population DESC;

```

### Q4: Highly Dominant Languages

Lists all languages spoken in their respective countries with a prevalence/percentage greater than 89%, sorted by dominance.

```sql
SELECT countries.name,
       languages.language,
       languages.percentage
FROM countries
     JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

```

### Q5: High-Density (Small but Populous) Countries

Filters out countries with a small physical footprint (Surface Area below 501) but maintaining a substantial population size (greater than 100,000).

```sql
SELECT countries.name,
       countries.surface_area,
       countries.population
FROM countries
WHERE surface_area < 501
  AND population > 100000;

```

### Q6: Advanced Constitutional Monarchies

Selects countries governed strictly under a Constitutional Monarchy that meet specific geographic and demographic baselines (Capital ID over 200 and a high Life Expectancy exceeding 75 years).

```sql
SELECT c.name,
       c.government_form,
       c.capital,
       c.life_expectancy
FROM countries AS c
WHERE c.government_form = 'Constitutional Monarchy'
  AND c.capital > 200
  AND c.life_expectancy > 75;

```

### Q7: Cities in Buenos Aires District (Argentina)

Displays the country name, city name, district, and population for cities located inside Argentina, specifically filtered down to the 'Buenos Aires' district with populations exceeding 500,000.

```sql
SELECT c.name AS country_name,
       ci.name AS city_name,
       ci.district,
       ci.population
FROM countries AS c
     JOIN cities AS ci ON c.id = ci.country_id
WHERE c.name = 'Argentina'
  AND ci.district = 'Buenos Aires'
  AND ci.population > 500000;

```

### Q8: Country Distribution per Region

Summarizes the total number of individual countries located across different global geographic regions, sorted in descending order by country count.

```sql
SELECT region,
       COUNT(countries.name) AS countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;

```

---

## Database Key Concepts Demonstrated

- **Table Aliasing:** Utilized in Q6 and Q7 (`FROM countries AS c`) to maintain readable and clean join relationships.
- **Data Aggregation:** Showcases `COUNT()` and `GROUP BY` functions to compile operational statistics out of raw, individual table records.
- **Multi-Conditional Filtering:** Applies numerical and text-matching filters (`AND`, `>`, `<`) within standard `WHERE` clauses to pinpoint explicit slices of data.

```

```
