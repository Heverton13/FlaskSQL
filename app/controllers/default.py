import os

from app import app
from app import db
from flask import render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from app.models.tables import Pessoa


@app.route("/", methods=["GET","POST"])
def index():
    if request.form:
        try:         
                pessoa = Pessoa(name=request.form.get("nome"), 
                        cpf=request.form.get("cpf"),
                        idade=request.form.get("idade"))
                db.session.add(pessoa)
                db.session.commit()
        except:
                abort(404)
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

""" @app.route("/delete", methods=["POST"])
def """

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

