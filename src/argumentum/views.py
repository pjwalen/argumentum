import datetime
from flask import render_template, redirect, url_for
from argumentum import app, db
from argumentum.models import Argument, Premise, Rebuttal
from argumentum.forms import ArgumentForm, PremiseForm


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: Add URL parameters for flagging invalid form fields.
    argumentform = ArgumentForm()
    if argumentform.validate_on_submit():
        argument = Argument()
        argument.title = argumentform.title.data
        argument.description = argumentform.description.data
        argument.left_opponent = argumentform.left_opponent.data
        argument.right_opponent = argumentform.right_opponent.data
        argument.created = datetime.datetime.now()
        argument.updated = datetime.datetime.now()
        db.session.add(argument)
        db.session.commit()
        return redirect(url_for('index'))
    arguments = Argument.query.all()
    return render_template('index.j2', arguments=arguments, argumentform=argumentform)


@app.route('/argument/<int:argumentid>', methods=['GET', 'POST'])
def argument(argumentid):
    argument = Argument.query.filter_by(id=argumentid).first_or_404()
    premiseform = PremiseForm()
    if premiseform.validate_on_submit():
        premise = Premise()
        premise.opponent = premiseform.opponent.data
        premise.argumentid = premiseform.argumentid.data
        premise.text = premiseform.text.data
        db.session.add(premise)
        db.session.commit()
        return redirect(url_for('argument', argumentid=argumentid))
    # TODO: Flush out this function. This is just a stub so far.
    return render_template('argument.j2', argument=argument, premiseform=premiseform)
