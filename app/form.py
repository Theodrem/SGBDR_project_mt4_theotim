from wtforms import Form, StringField, IntegerField, SelectField, SubmitField
from flask_wtf import FlaskForm


class AttributeForm(FlaskForm):
    order_by = SelectField(
        'order_by',
        default="title",
        choices=[
            ('title', 'Titre'),
            ('category.name', 'Categorie'),
            ('rental', 'Nombre de location'),
        ],
    )
    order = SelectField(
        'order',
        default="ASC",
        choices=[('ASC', 'Croissant'), ('DESC', 'Décroissant')],
    )
    limit = SelectField(
        'order',
        default=10,
        choices=[(10, 10), (25, 25), (50, 50), (100, 100)],
    )
    submit = SubmitField('Submit')
