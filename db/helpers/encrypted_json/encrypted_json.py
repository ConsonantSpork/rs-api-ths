import json

from flask import current_app
from sqlalchemy import types

from .crypto import decrypt, encrypt


class EncryptedJSON(types.TypeDecorator):
    """JSON type, stores data as encrypted bytes and handles conversion."""

    impl = types.LargeBinary

    def process_bind_param(self, value, dialect):
        if value is not None:
            json_str = json.dumps(value)
            value = encrypt(current_app.config['SECRET_KEY'], json_str)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            decrypted = decrypt(current_app.config['SECRET_KEY'], value)
            value = json.loads(decrypted)
        return value
