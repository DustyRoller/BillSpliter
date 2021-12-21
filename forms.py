from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, StringField
from wtforms.validators import DataRequired

class AddTransactionForm(FlaskForm):
    attendees = StringField("Attendees:", validators=[DataRequired(message="A list of attendees is required")])
    cost = DecimalField("Cost:", validators=[DataRequired(message="A cost is required")])
    # The date value will get returned from the page in YYYY-MM-DD format so allow that here.
    date = DateField("Date:", format="%Y-%m-%d", validators=[DataRequired(message="A date is required")])
    payer = StringField("Payer:", validators=[DataRequired(message="A payer is required")])
    venue = StringField("Venue:", validators=[DataRequired(message="A venue is required")])
