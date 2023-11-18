#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Changes the name of a State object from the database hbtn_0e_6_usa
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

    # Query to retrieve the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the State object with id = 2 exists
    if state_to_update:
        # Update the name of the State object
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()

