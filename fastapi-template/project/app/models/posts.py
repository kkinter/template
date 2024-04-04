from app.db_con import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
