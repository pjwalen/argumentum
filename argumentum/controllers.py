import datetime
from urllib.parse import urlparse
from flask import render_template, redirect, request
from argumentum import application, db
from argumentum.models import Argument, Premise, Evidence
from argumentum.forms import ArgumentCreateForm, ArgumentDeleteForm, ArgumentUpdateForm, PremiseCreateForm, \
    PremiseDeleteForm, PremiseUpdateForm, EvidenceCreateForm, EvidenceUpdateForm, EvidenceDeleteForm


@application.route('/')
def index():
    # TODO: Add URL parameters for flagging invalid form fields.
    argumentcreateform = ArgumentCreateForm()
    argumentupdateform = ArgumentUpdateForm()
    argumentdeleteform = ArgumentDeleteForm()
    arguments = Argument.query.all()
    update_argument_id = request.args.get('update_argument_id', type=int)
    return render_template(
        'index.html',
        arguments=arguments,
        argumentcreateform=argumentcreateform,
        argumentupdateform=argumentupdateform,
        argumentdeleteform=argumentdeleteform,
        update_argument_id=update_argument_id
    )


@application.route('/argument/<int:argumentid>')
def argument_get(argumentid):
    argument = Argument.query.filter_by(id=argumentid).first_or_404()
    premisecreateform = PremiseCreateForm()
    premisedeleteform = PremiseDeleteForm()
    evidencecreateform = EvidenceCreateForm()
    evidencedeleteform = EvidenceDeleteForm()
    evidenceupdateform = EvidenceUpdateForm()
    create_premise_id = request.args.get('create_premise_id', type=int)
    create_evidence_id = request.args.get('create_evidence_id', type=int)
    update_evidence_id = request.args.get('update_evidence_id', type=int)
    return render_template(
        'argument.html',
        argument=argument,
        premisecreateform=premisecreateform,
        premisedeleteform=premisedeleteform,
        evidencecreateform=evidencecreateform,
        evidencedeleteform=evidencedeleteform,
        evidenceupdateform=evidenceupdateform,
        create_premise_id=create_premise_id,
        create_evidence_id=create_evidence_id,
        update_evidence_id=update_evidence_id
    )


@application.route('/argument', methods=['POST'])
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
    return redirect(urlparse(request.referrer).path)


@application.route('/argument/update', methods=['POST'])
def argument_update():
    argumentform = ArgumentUpdateForm()

    if argumentform.validate_on_submit():
        argument = Argument.query.filter_by(id=argumentform.argumentid.data).first_or_404()
        argument.title = argumentform.title.data
        argument.description = argumentform.description.data
        argument.left_opponent = argumentform.left_opponent.data
        argument.right_opponent = argumentform.right_opponent.data
        argument.updated = datetime.datetime.now()
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/argument/delete', methods=['POST'])
def argument_delete():
    argumentform = ArgumentDeleteForm()
    if argumentform.validate_on_submit():
        argument = Argument.query.filter_by(id=argumentform.argumentid.data).first_or_404()
        db.session.delete(argument)
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/premise', methods=['POST'])
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
    return redirect(urlparse(request.referrer).path)


@application.route('/premise/update', methods=['POST'])
def premise_update():
    premiseform = PremiseUpdateForm()
    if premiseform.validate_on_submit():
        premise = Premise.query.filter_by(id=premiseform.premiseid.data).first_or_404()
        premise.text = premiseform.text.data
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/premise/delete', methods=['POST'])
def premise_delete():
    form = PremiseDeleteForm()
    if form.validate_on_submit():
        premise = Premise.query.filter_by(id=form.premiseid.data).first_or_404()
        db.session.delete(premise)
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/evidence', methods=['POST'])
def evidence_create():
    form = EvidenceCreateForm()
    if form.validate_on_submit():
        evidence = Evidence()
        evidence.text = form.text.data
        evidence.premiseid = form.premiseid.data
        db.session.add(evidence)
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/evidence/update', methods=['POST'])
def evidence_update():
    evidenceform = EvidenceUpdateForm()
    if evidenceform.validate_on_submit():
        evidence = Evidence.query.filter_by(id=evidenceform.evidenceid.data).first_or_404()
        evidence.text = evidenceform.text.data
        db.session.commit()
    return redirect(urlparse(request.referrer).path)


@application.route('/evidence/delete', methods=['POST'])
def evidence_delete():
    form = EvidenceDeleteForm()
    if form.validate_on_submit():
        evidence = Evidence.query.filter_by(id=form.evidenceid.data).first_or_404()
        db.session.delete(evidence)
        db.session.commit()
    return redirect(urlparse(request.referrer).path)
