from flask import Blueprint

runner = Blueprint('runner',__name__,template_folder='templates',url_prefix='/runner')

from .routes import *