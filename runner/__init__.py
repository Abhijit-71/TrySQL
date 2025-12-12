from flask import Blueprint

runner = Blueprint('runner',__name__,template_folder='templates')

from .routes import *