from contextlib import contextmanager

from ..db import Session


__all__ = ['session_scope']


@contextmanager
def session_scope():
    """Decorator to automatically close or rollback session."""

    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
