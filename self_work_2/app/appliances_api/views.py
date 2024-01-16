from app import db
from flask import request
from flask_restful import Resource
from app.appliances_api.models import Appliance
from .schemas.appliances import ApplianceSchema


class AppliancesApi(Resource):
    def get(self):
        schema = ApplianceSchema(many=True)
        appliances = Appliance.query.all()
        return {"appliances": schema.dump(appliances)}

    def post(self):
        schema = ApplianceSchema()
        appliance = schema.load(request.json)
        db.session.add(appliance)
        db.session.commit()
        return {"appliance": schema.dump(appliance)}


class ApplianceApi(Resource):
    def get(self, id):
        schema = ApplianceSchema(partial=True)
        appliance = Appliance.query.filter_by(id=id).first_or_404(description='Appliance not found.')
        return schema.dump(appliance)

    def put(self, id):
        schema = ApplianceSchema(partial=True)
        appliance = Appliance.query.filter_by(id=id).first_or_404(description='Appliance not found.')
        appliance = schema.load(request.json, instance=appliance)
        db.session.add(appliance)
        db.session.commit()
        return {"appliance": schema.dump(appliance)}

    def delete(self, id):
        schema = ApplianceSchema()
        appliance = Appliance.query.filter_by(id=id).first_or_404(description='Appliance not found.')
        db.session.delete(appliance)
        db.session.commit()
        return {"appliance": schema.dump(appliance), "message": f"Appliance {appliance.title} deleted"}