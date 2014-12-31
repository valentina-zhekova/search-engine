from connection import Base
from sqlalchemy import Column, Integer, String, Bool


class Page(Base):
    __tablename__ = "Pages"
    id = Column(Integer, primary_key=True)
    website_id = Column(Integer)
    url = Column(String)
    title = Column(String)
    description = Column(String)
    # ads = Column(...)
    SSL = Column(Bool)  # is there such a thing?
    points = Column(Integer)
    multy_languages = Column(Integer)  # rough count???
