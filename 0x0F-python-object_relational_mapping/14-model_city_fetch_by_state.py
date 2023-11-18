#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    """
    Prints all City objects from the database hbtn_0e_14_usa
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

if __name__ == "__main__":
    main()
