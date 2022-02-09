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
        label="Trier par",
    )
    order = SelectField(
        'order',
        default="ASC",
        choices=[('ASC', 'Ascendant'), ('DESC', 'Déscendant')],
        label="Ordre des résultats",
    )

    limit = SelectField(
        'limit',
        default=10,
        choices=[(10, 10), (25, 25), (50, 50), (100, 100)],
        label="Nombre de résultat",
    )
    submit = SubmitField('Submit')
