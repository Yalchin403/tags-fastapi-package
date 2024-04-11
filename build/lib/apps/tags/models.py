from sqlalchemy import Column, Integer, String

from apps.core.db import Base



class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
