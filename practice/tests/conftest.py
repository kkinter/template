import os
from typing import Generator

import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from storeapi.deps import get_db
from storeapi.post import router as post_router


@pytest.fixture(scope="session")
def db() -> Generator:
    engine = create_engine(os.environ.get("TEST_DATABASE_URL"))
    with engine.begin():
        alembic_config = AlembicConfig("alembic.ini")
        alembic_config.config_ini_section = "testdb"
        alembic_upgrade(alembic_config, "head")

    SessionTest = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    _db = SessionTest()
    try:
        yield _db
    finally:
        # teardown table
        # from storeapi import models

        # _Base = models.Base
        # for table in reversed(_Base.metadata.sorted_tables):
        #     _db.execute(table.delete())
        # _db.commit()
        # _db.close()
        engine.dispose()


# lambda arguments: expression
# lambda <no arg> : db
# get_db 함수가 호출될 때마다 `db를 반환`
@pytest.fixture(scope="module")
def client_with_db(db) -> Generator:
    app = FastAPI()
    app.include_router(post_router)
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def client() -> Generator:
    app = FastAPI()
    app.include_router(post_router)
    with TestClient(app) as client:
        yield client
