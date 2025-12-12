from flask import request , jsonify , render_template
from runner import runner


@runner.route("/runner", methods=["POST"])
def sql_runner():
    data = request.get_json()
    return jsonify(f"ran successfully : {data}") , 200

@runner.route("/hello")
def hello():
    return render_template('index.html')