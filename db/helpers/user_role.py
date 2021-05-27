import enum

from sqlalchemy import types


class UserRoleEnum(enum.Enum):
    GLOBAL_ADMIN = 1
    LOCAL_ADMIN = 2
    OPERATOR = 3
    USER = 4


class UserRole(types.TypeDecorator):
    """User role column, handles conversion to and from UserRoleEnum."""

    impl = types.SMALLINT

    def process_bind_param(self, value, dialect):
        return getattr(value, 'value', None)

    def process_result_value(self, value, dialect):
        if value is not None:
            value = UserRoleEnum(value)
        return value
