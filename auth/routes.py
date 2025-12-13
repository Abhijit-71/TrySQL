from flask import request , jsonify , render_template
from auth import auth
from app.models import db , User
from flask_jwt_extended import create_access_token , set_access_cookies

@auth.route("/reg-api",methods=["POST"])
def reg_api():
    data = request.get_json()
    print(data)
    if data["password"] != data["password2"]:
        return {'message':'Password not matched'} , 400
    
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "Username already taken"}), 400
    
    new_user = User(username=data["username"], password=data["password"]) #type:ignore
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201
    
        

@auth.route("/login-api",methods=["POST"])
def login_api():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or password != user.password:
        return jsonify({"msg": "Invalid username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.id))
    resp = jsonify({"msg": "login successful"},200)
    set_access_cookies(resp,access_token)
    return resp, 200





@auth.route("/register")
def register():
    return render_template('register.html')

@auth.route("/login")
def login():
    return render_template('login.html')