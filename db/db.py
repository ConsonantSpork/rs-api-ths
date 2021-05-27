from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import DATABASE_URL


__all__ = ['engine', 'Session', 'Base']

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
