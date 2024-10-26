from sqlalchemy import Column, Text, TIMESTAMP, func, Integer
from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(Text, nullable=False, default='')
    email = Column(Text, nullable=False, default='')
    token = Column(Text, nullable=False, default='')
    refresh_token = Column(Text, nullable=False, default='')
    google_uid = Column(Text, nullable=False, default='')
    created_at = Column(TIMESTAMP(timezone=True), default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=func.now())
