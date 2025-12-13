from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
from .models import db

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_PATH"] = "/"
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # TEMP: disable while testing
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=14)

jwt_man = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()


from .routes import *