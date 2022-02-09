from flask import request, render_template, redirect, url_for
from app.db.connector_db import Connector
from flask_paginate import Pagination
from app.form import AttributeForm
from app import app

# 1st %s = Limit results
# 2nd %s = Order by results
# 3rd %s = Order results
# 4th %s = Limit results
# 5th %s = Offset results

REQ = {
    "REQ": "SELECT distinct film.title ,"
    " film.rental_rate, category.name, film.rating,"
    "floor(COUNT(*) OVER() / %s) as nb_pages,"
    " COUNT(title) as rental FROM film"
    " JOIN film_category ON (film.film_id = film_category.film_id)"
    " JOIN category ON (category.category_id = film_category.category_id)"
    " JOIN inventory ON ( film.film_id = inventory.film_id)"
    " JOIN rental  ON ( rental.inventory_id = inventory.inventory_id)"
    " GROUP BY title"
    " ORDER BY %s %s"
    " LIMIT %s OFFSET %s"
}


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: The template of the index website
    """
    form = AttributeForm(request.form)

    if form.validate_on_submit():
        order_by = form.order_by.data
        order = form.order.data
        limit = form.limit.data
        print(order_by, order, limit)
        return redirect(
            url_for("index", order_by=order_by, order=order, limit=limit)
        )

    order_by = request.args.get('order_by', default="title")
    order = request.args.get('order', default="")
    limit = request.args.get('limit', default=10)

    page = request.args.get('page', default=0)
    offset = int(limit) * int(page)
    movie_request = REQ['REQ'] % (limit, order_by, order, limit, offset)

    c = Connector()
    data = c.fetch_rows(movie_request)
    c.close()

    nb_pages = data[0]['nb_pages']
    nb_pages *= int(limit)
    pagination = Pagination(page=page, total=int(nb_pages), per_page=limit)

    return render_template(
        "index.html",
        form=form,
        data=data,
        page=page,
        nb_pages=int(nb_pages),
        pagination=pagination,
    )
