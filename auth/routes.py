from flask import request , jsonify , render_template , redirect
from flask_jwt_extended import create_access_token , set_access_cookies , unset_access_cookies , jwt_required , verify_jwt_in_request
from auth import auth
from app.models import db , User


# register api routes
@auth.route("/reg-api",methods=["POST"])
def reg_api():
        
    data = request.get_json()
    if data["password"] != data["password2"]:
        return {'message':'Password not matched'} , 400
    
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "Username already taken"}), 400
    
    new_user = User(username=data["username"].strip(), password=data["password"].strip()) #type:ignore
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201
    
        
# register api routes
@auth.route("/login-api",methods=["POST"])
def login_api():
    
    data = request.get_json()
    username = data.get("username").strip()
    password = data.get("password").strip()

    user = User.query.filter_by(username=username).first()

    if not user or password != user.password:
        return jsonify({"msg": "Invalid username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.id))
    resp = jsonify({"msg": "login successful"},200)
    set_access_cookies(resp,access_token)
    return resp


@auth.route("/logout-api", methods=["POST"])
@jwt_required()
def logout_api():
    resp = jsonify({"msg": "logged out"})
    unset_access_cookies(resp)
    return resp, 200



#page serving routes

@auth.route("/register")
def register():
    try:
        verify_jwt_in_request()
        return redirect("/runner/dashboard")
    except:
        return render_template('register.html')

@auth.route("/login")
def login():
    try:
        verify_jwt_in_request()
        return redirect("/runner/dashboard")
    except:
        return render_template('login.html')