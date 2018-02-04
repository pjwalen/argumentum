import datetime
from flask import render_template, redirect, request
from argumentum import app, db
from argumentum.models import Argument, Premise, Evidence
from argumentum.forms import ArgumentCreateForm, PremiseCreateForm, PremiseDeleteForm, EvidenceCreateForm, EvidenceDeleteForm


@app.route('/')
def index():
    # TODO: Add URL parameters for flagging invalid form fields.
    argumentcreateform = ArgumentCreateForm()
    arguments = Argument.query.all()
    return render_template('index.jinja2', arguments=arguments, argumentcreateform=argumentcreateform)


@app.route('/argument/<int:argumentid>')
def argument_get(argumentid):
    argument = Argument.query.filter_by(id=argumentid).first_or_404()
    premisecreateform = PremiseCreateForm()
    premisedeleteform = PremiseDeleteForm()
    evidencecreateform = EvidenceCreateForm()
    evidencedeleteform = EvidenceDeleteForm()
    return render_template(
        'argument.jinja2',
        argument=argument,
        premisecreateform=premisecreateform,
        premisedeleteform=premisedeleteform,
        evidencecreateform=evidencecreateform,
        evidencedeleteform=evidencedeleteform
    )


@app.route('/argument', methods=['POST'])
def argument_create():
    argumentform = ArgumentCreateForm()
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
    return redirect(request.referrer)


@app.route('/argument/update', methods=['POST'])
def argument_update():
    pass


@app.route('/argument/delete', methods=['POST'])
def argument_delete():
    pass


@app.route('/premise', methods=['POST'])
def premise_create():
    premiseform = PremiseCreateForm()
    if premiseform.validate_on_submit():
        premise = Premise()
        premise.opponent = premiseform.opponent.data
        premise.argumentid = premiseform.argumentid.data
        premise.parent = premiseform.parent.data
        premise.text = premiseform.text.data
        db.session.add(premise)
        db.session.commit()
    return redirect(request.referrer)


@app.route('/premise/update', methods=['POST'])
def premise_update():
    pass


@app.route('/premise/delete', methods=['POST'])
def premise_delete():
    form = PremiseDeleteForm()
    if form.validate_on_submit():
        premise = Premise.query.filter_by(id=form.premiseid.data).first_or_404()
        db.session.delete(premise)
        db.session.commit()
    return redirect(request.referrer)


@app.route('/evidence', methods=['POST'])
def evidence_create():
    form = EvidenceCreateForm()
    if form.validate_on_submit():
        evidence = Evidence()
        evidence.text = form.text.data
        evidence.premiseid = form.premiseid.data
        db.session.add(evidence)
        db.session.commit()
    return redirect(request.referrer)


@app.route('/evidence/update', methods=['POST'])
def evidence_update():
    pass


@app.route('/evidence/delete', methods=['POST'])
def evidence_delete():
    form = EvidenceDeleteForm()
    if form.validate_on_submit():
        evidence = Evidence.query.filter_by(id=form.evidenceid.data).first_or_404()
        db.session.delete(evidence)
        db.session.commit()
    return redirect(request.referrer)
