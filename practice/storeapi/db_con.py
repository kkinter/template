from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from storeapi.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
