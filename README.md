## REQUETE SQL
```sql 
SELECT distinct film.title ,
film.replacement_cost, category.name, film.rating,
floor(COUNT(*) OVER() / 5) as nb_pages,
COUNT(title) as rental FROM film
JOIN film_category ON (film.film_id = film_category.film_id)
JOIN category ON (category.category_id = film_category.category_id)
JOIN inventory ON ( film.film_id = inventory.film_id)
JOIN rental  ON ( rental.inventory_id = inventory.inventory_id)
GROUP BY title
ORDER BY {title} {ASC}
LIMIT 5 OFFSET 5 
```

**Paramètres**

On peut utiliser le formulaire ou la barre de l'url

Exemple: http://127.0.0.1:5000/?order_by=title&order=DESC&limit=22&page=1