from storeapi.db_con import SessionLocal


def get_db():
    db = SessionLocal()
    print("session 호출")
    try:
        yield db
    finally:
        print("session 닫힘")
        db.close()
