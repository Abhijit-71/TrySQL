import json
from urllib.request import urlopen
from flask import request , jsonify , render_template
from flask_jwt_extended import jwt_required , get_jwt_identity
from runner import runner
from .sql_shell import sql_runner
from app.models import User


@runner.route("/quote")
@jwt_required()
def quote():
    with urlopen("https://zenquotes.io/api/random") as r:
        data = json.loads(r.read().decode())
    return jsonify(data),200



#sql_runner api io route
@runner.route("/io",methods=["POST"])
@jwt_required()
def run_sql():
    cmd = request.get_json()["command"]
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=int(user_id)).first()
    output = sql_runner(user.username,cmd) #type:ignore
    output_final = {"output": output, "status": "success"}
    return jsonify(output_final) , 200


#sql_shell route
@runner.route("/shell")
@jwt_required()
def shell():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=int(user_id)).first()
    username = user.username #type:ignore
    return render_template('shell.html',username=username)


# dashboard route
@runner.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=int(user_id)).first()
    username = user.username #type:ignore
    return render_template('dashboard.html',username=username)
