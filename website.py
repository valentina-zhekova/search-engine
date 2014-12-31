from connection import Base
from sqlalchemy import Column, Integer, String


class Website(Base):
    __tablename__ = "Websites"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    domain = Column(String)
    pages_count = Column(Integer)
    HTML_version = Column(String)
