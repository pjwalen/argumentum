from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Optional, AnyOf


class ArgumentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    left_opponent = StringField('Left Opponent', validators=[DataRequired()])
    right_opponent = StringField('Right Opponent', validators=[DataRequired()])
    description = StringField('Description', validators=[Optional()])


class PremiseForm(FlaskForm):
    argumentid = IntegerField('Argument ID', validators=[DataRequired()], widget=HiddenInput())
    opponent = StringField('Opponent', validators=[DataRequired(), AnyOf(['left', 'right'])], widget=HiddenInput())
    parent = IntegerField('Premise ID', validators=[Optional()], widget=HiddenInput())
    text = StringField('Text', validators=[DataRequired()])


class EvidenceForm(FlaskForm):
    act = StringField('Action', validators=[AnyOf(['create', 'delete'])], widget=HiddenInput())
    premiseid = IntegerField('Premise ID', validators=[DataRequired()], widget=HiddenInput())
    text = StringField('Text')
