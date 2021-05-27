from flask_restful import Resource

from app.extensions import flask_httpauth as auth


class DeviceDataResource(Resource):
    @auth.login_required
    def get(self):
        return 'hello, world'
