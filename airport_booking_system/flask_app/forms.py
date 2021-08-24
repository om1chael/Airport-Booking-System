from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError


class AddPassengerForm(FlaskForm):
    name = StringField('Customer Name', validators=[DataRequired(), Length(min=1, max=50)])
    passportid = StringField('psw', validators=[DataRequired(), Length(9)])

    def validate_name(form, field):
        if not field.name.isalpha():
            raise ValidationError("Please input letters only")



class CreateFlightForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), Length(min=1, max=7)])
    destination = StringField('destination', validators=[DataRequired()])
    time = StringField('time', validators=[DataRequired()])
    duration = IntegerField('duration', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])

    def validate_id(form, field):
        if not field.id.isalpha():
            raise ValidationError("Please input letters only")

