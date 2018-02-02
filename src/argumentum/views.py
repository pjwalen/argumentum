import datetime
from flask import render_template, redirect, url_for
from argumentum import app, db
from argumentum.models import Argument, Premise, Evidence
from argumentum.forms import ArgumentForm, PremiseForm, EvidenceForm


@app.route('/')
def index():
    # TODO: Add URL parameters for flagging invalid form fields.
    argumentform = ArgumentForm()
    arguments = Argument.query.all()
    return render_template('index.j2', arguments=arguments, argumentform=argumentform)


@app.route('/argument', methods=['POST'])
def argument_post():
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


@app.route('/argument/<int:argumentid>')
def argument_get(argumentid):
    argument = Argument.query.filter_by(id=argumentid).first_or_404()
    premiseform = PremiseForm()
    evidenceform = EvidenceForm()
    return render_template('argument.j2', argument=argument, premiseform=premiseform, evidenceform=evidenceform)


@app.route('/argument/<int:argumentid>/premise', methods=['POST'])
def premise_post(argumentid):
    premiseform = PremiseForm()
    if premiseform.validate_on_submit():
        premise = Premise()
        premise.opponent = premiseform.opponent.data
        premise.argumentid = premiseform.argumentid.data
        premise.parent = premiseform.parent.data
        premise.text = premiseform.text.data
        db.session.add(premise)
        db.session.commit()
    return redirect(url_for('argument_get', argumentid=argumentid))


@app.route('/argument/<int:argumentid>/evidence', methods=['POST'])
def evidence_post(argumentid):
    evidenceform = EvidenceForm()
    if evidenceform.validate_on_submit():
        if evidenceform.act.data == 'create':
            evidence = Evidence()
            evidence.text = evidenceform.text.data
            evidence.premiseid = evidenceform.premiseid.data
            db.session.add(evidence)
            db.session.commit()
        elif evidenceform.act.data == 'delete':
            evidence = Evidence.query.filter_by(id=evidenceform.premiseid.data).one()
            db.session.delete(evidence)
            db.session.commit()
    return redirect(url_for('argument_get', argumentid=argumentid))
