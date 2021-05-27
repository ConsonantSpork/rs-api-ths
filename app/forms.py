from wtforms import Form, StringField, PasswordField, validators, TextAreaField, IntegerField, BooleanField


class LoginPassword(Form):
    login = StringField('Login', [validators.Length(min=4, max=128)])
    password = PasswordField('Password', [validators.data_required()])


class ConversionAdd(Form):
    name = StringField('Name', [validators.Length(min=1, max=128)])
    description = TextAreaField('Description')
    source = TextAreaField('Source', [validators.data_required()])


class DaemonConfig(Form):
    query_interval = IntegerField('Query Interval', [validators.NumberRange(1, 60)])
    enabled = BooleanField('Enabled', [validators.data_required()])
