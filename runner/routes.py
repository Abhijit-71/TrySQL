from flask import request , jsonify , render_template
from runner import runner


@runner.route("/input", methods=["POST"])
def sql_runner():
    data = request.get_json()
    return jsonify(f"ran successfully : {data}") , 200

@runner.route("/shell")
def runner_():
    return render_template('shell.html')