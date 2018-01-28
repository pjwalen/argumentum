import datetime
from flask import render_template, redirect, url_for
from argumentum import app, db
from argumentum.models import Argument, Opponent, Premise, Rebuttal
from argumentum.forms import ArgumentForm


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: Add URL parameters for flagging invalid form fields.
    argumentform = ArgumentForm()
    if argumentform.validate_on_submit():
        argument = Argument()
        argument.title = argumentform.title.data
        argument.description = argumentform.description.data
        argument.created = datetime.datetime.now()
        argument.updated = datetime.datetime.now()
        db.session.add(argument)
        db.session.commit()
        return redirect(url_for('index'))
    arguments = Argument.query.all()
    return render_template('index.j2', arguments=arguments, argumentform=argumentform)


@app.route('/argument/<int:argumentid>')
def argument(argumentid):
    # TODO: Flush out this function. This is just a stub so far.
    return str(argumentid)
