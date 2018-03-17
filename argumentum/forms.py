from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Optional, AnyOf


class ArgumentCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    left_opponent = StringField('Left Opponent', validators=[DataRequired()])
    right_opponent = StringField('Right Opponent', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])


class ArgumentDeleteForm(FlaskForm):
    argumentid = IntegerField('Argument ID', validators=[DataRequired()], widget=HiddenInput())


class ArgumentUpdateForm(FlaskForm):
    argumentid = IntegerField('Argument ID', validators=[DataRequired()], widget=HiddenInput())
    title = StringField('Argument Text', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    left_opponent = StringField('Left Opponent', validators=[DataRequired()])
    right_opponent = StringField('Right Opponent', validators=[DataRequired()])


class PremiseCreateForm(FlaskForm):
    argumentid = IntegerField('Argument ID', validators=[DataRequired()], widget=HiddenInput())
    opponent = SelectField('Opponent', choices=[('left', 'left'), ('right', 'right')])
    parent = IntegerField('Premise ID', validators=[Optional()], widget=HiddenInput())
    text = TextAreaField('Text', validators=[DataRequired()])


class PremiseDeleteForm(FlaskForm):
    premiseid = IntegerField('Premise ID', validators=[DataRequired()], widget=HiddenInput())


class PremiseUpdateForm(FlaskForm):
    premiseid = IntegerField('Premise ID', validators=[DataRequired()], widget=HiddenInput())
    text = TextAreaField('Premise Text', validators=[DataRequired()])


class EvidenceCreateForm(FlaskForm):
    premiseid = IntegerField('Premise ID', validators=[DataRequired()], widget=HiddenInput())
    text = StringField('Text', validators=[DataRequired()])


class EvidenceUpdateForm(FlaskForm):
    evidenceid = IntegerField('Evidence ID', validators=[DataRequired()], widget=HiddenInput())
    text = StringField('Text', validators=[DataRequired()])


class EvidenceDeleteForm(FlaskForm):
    evidenceid = IntegerField('Evidence ID', validators=[DataRequired()], widget=HiddenInput())
