from marshmallow import fields, validate, validates_schema, ValidationError
from app import ma
from marshmallow.validate import Length, Regexp, Range
from app.appliances_api.models import Appliance


class ApplianceSchema(ma.SQLAlchemyAutoSchema):

    title =  fields.String(required=True, validate=[validate.Length(min=4, max=30)])
    description = fields.String(required=True, validate=[validate.Length(min=10, max=250)])
    producer = fields.String(required=True, validate=[validate.Length(min=1, max=30)])
    sku = fields.Integer(required=True, validate=[Range(min=0)])
    price = fields.Float(required=True, validate=[Range(min=0)])
    manufacturing_date =  fields.DateTime(required=False)



    @validates_schema
    def validate_id(self, data, **kwargs):
        id = data.get("id")
        if id is not None:
            raise ValidationError("Unknown field.", "id")
        
    @validates_schema
    def validate_sku(self, data, **kwargs):
        sku = data.get("sku")
        if sku is not None and Appliance.query.filter_by(sku=sku).first():
            raise ValidationError(f"SKU {sku} already exists")

    class Meta:
        model = Appliance
        load_instance = True