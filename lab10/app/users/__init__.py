from flask import Blueprint

users_blueprint = Blueprint('users', __name__, template_folder="templates/users")

from . import views