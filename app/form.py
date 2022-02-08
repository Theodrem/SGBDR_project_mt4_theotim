from wtforms import Form, StringField, IntegerField, SelectField, SubmitField
from flask_wtf import FlaskForm


class AttributeForm(FlaskForm):
    order_by = SelectField(
        'order_by',
        default="title",
        choices=[
            ('title', 'Titre'),
            ('category.name', 'Categorie'),
            ('rating', 'Classement'),
        ],
    )
    order = SelectField(
        'order',
        default="ASC",
        choices=[('ASC', 'Croissant'), ('DESC', 'Décroissant')],
    )
    limit = IntegerField('limit', default=10)
    submit = SubmitField('Submit')
