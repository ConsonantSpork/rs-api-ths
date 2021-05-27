import bcrypt as bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship

from .db import Base
from .helpers import UserRole
from .helpers.encrypted_json.encrypted_json import EncryptedJSON

__all__ = ['User', 'Device', 'Converter']


class User(Base, UserMixin):
    """User model.

    Attributes
    ----------
    login : str
    password : str

    Methods
    -------
    hash_password(str)
        hashes provided password for safe validation
    check_password(str)
        checks that provided string is equal to password
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(128), index=True,
                   unique=True, nullable=False)
    password = Column(LargeBinary(128), nullable=False)
    role = Column(UserRole, nullable=False)

    def __repr__(self):
        return f"<User(login={self.login}, role={self.role})>"

    def hash_password(self, password):
        """Hash password for safe validatoin.

        Parameters
        ----------
        password : str
            password to hash
        """

        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode('utf8'), salt)

    def check_password(self, password):
        """Check password against stored hash.

        Parameters
        ----------
        password : str
            password to check

        Returns
        -------
        bool
            whether the check succeeded
        """

        return bcrypt.checkpw(password.encode('utf8'), self.password)


device_to_converter = Table('device_to_converter', Base.metadata,
                            Column('device_id', Integer, ForeignKey('devices.id')),
                            Column('converter_id', Integer, ForeignKey('converters.id'))
                            )


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    connection_params = Column(EncryptedJSON)
    converters = relationship('Converter', secondary=device_to_converter)


class Converter(Base):
    __tablename__ = 'converters'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    source_code = Column(String, nullable=False)


class DaemonConfig:
    __tablename__ = 'daemon_config'

    id = Column(Integer, primary_key=True)
    query_interval = Column(Integer, nullable=False)
    enabled = Column(Boolean, nullable=False)
