from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit'
)


class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd1'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd1" contains invalid value')
        if values['cmd2'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd2" contains invalid value')

        return values
