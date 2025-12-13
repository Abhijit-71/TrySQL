from flask import request , jsonify , render_template
from runner import runner
from .sql_shell import sql_runner
from app.models import User
from flask_jwt_extended import jwt_required , get_jwt_identity

@runner.route("/io",methods=["POST"])
@jwt_required()
def run_sql():
    cmd = request.get_json()["command"]
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=int(user_id)).first()
    output = sql_runner(user.username,cmd) #type:ignore
    output_final = {"output": output, "status": "success"}
    return jsonify(output_final) , 200

@runner.route("/shell")
@jwt_required()
def shell():
    return render_template('shell.html')