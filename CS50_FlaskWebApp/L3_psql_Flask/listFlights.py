import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql:///swapnil")
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} with {flight.duration} minutes")
    return flights

if __name__ == '__main__':
    main()
