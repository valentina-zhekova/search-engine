from connection import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    engine = create_engine("sqlite:///websites_database.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)  # actually do I need this and the next line
    session.commit()

if __name__ == '__main__':
    main()
