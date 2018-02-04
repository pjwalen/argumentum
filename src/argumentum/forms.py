from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Optional, AnyOf


class ArgumentCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    left_opponent = StringField('Left Opponent', validators=[DataRequired()])
    right_opponent = StringField('Right Opponent', validators=[DataRequired()])
    description = StringField('Description', validators=[Optional()])


class PremiseCreateForm(FlaskForm):
    argumentid = IntegerField('Argument ID', validators=[DataRequired()], widget=HiddenInput())
    opponent = StringField('Opponent', validators=[DataRequired(), AnyOf(['left', 'right'])], widget=HiddenInput())
    parent = IntegerField('Premise ID', validators=[Optional()], widget=HiddenInput())
    text = StringField('Text', validators=[DataRequired()])


class EvidenceCreateForm(FlaskForm):
    premiseid = IntegerField('Premise ID', validators=[DataRequired()], widget=HiddenInput())
    text = StringField('Text')


class EvidenceDeleteForm(FlaskForm):
    evidenceid = IntegerField('Evidence ID', validators=[DataRequired()], widget=HiddenInput())
