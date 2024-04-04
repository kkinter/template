from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

PGDATABASE_URL = settings.PGDATABASE_URL

if settings.PGDATABASE_URL:
    engine = create_engine(
        settings.PGDATABASE_URL,
        pool_pre_ping=True,
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    if settings.ENVIRONMENT == "development":
        db_info = f"Using database at {settings.SQLALCHEMY_DATABASE_URI}"
        print(db_info)
else:
    raise ValueError("PGDATABASE_URL is not set")

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
