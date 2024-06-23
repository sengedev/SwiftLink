import datetime
from sqlalchemy import Column, String, DateTime
from database.db import Base
import uuid
import base64


class User(Base):
    __tablename__ = 'user'

    id = Column(String, default=lambda: base64.b64encode(str(uuid.uuid4()).encode()).decode(), primary_key=True,
                index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())


class ShortLink(Base):
    __tablename__ = 'short_links'

    id = Column(String, default=lambda: base64.b64encode(str(uuid.uuid4()).encode()).decode(), primary_key=True,
                index=True)
    route = Column(String, unique=True, index=True)
    url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())
