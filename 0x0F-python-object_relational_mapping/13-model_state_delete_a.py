#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Deletes all State objects with a name containing the letter "a"
    from the database hbtn_0e_6_usa
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1:]

    # Define the MySQL server connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to retrieve State objects with a name containing the letter "a"
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the retrieved State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()

