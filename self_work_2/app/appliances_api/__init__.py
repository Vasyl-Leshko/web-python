
from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from .views import AppliancesApi, ApplianceApi

appliance_api_bp = Blueprint("appliances_api", __name__, url_prefix="/api")
api = Api(appliance_api_bp)

api.add_resource(AppliancesApi, "/appliances")
api.add_resource(ApplianceApi, "/appliances/<int:id>")


@appliance_api_bp.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400