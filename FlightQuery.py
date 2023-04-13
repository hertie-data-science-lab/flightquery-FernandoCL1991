# TEAM MEMBERS: Augusto Fonseca, Rodrigo Dornelles, Danial Riaz, Fernando Corral

from SortedTableMap import *

'''An application of SortedTableMap, used to query tickets of expected period'''
class FlightQuery(SortedTableMap):
    # Class Key which is defined by four arguments: origin, dest, date, time
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        # Initializing instance variables for each Key
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        # Less than function
        def __lt__(self, other):
            # Check date
            if self._date < other._date:
                return True
            # Check date and time
            elif self._date == other._date and self._time < other._time:
                return True
            # Check date and time and origin
            elif self._date == other._date and self._time == other._time and self._origin < other._origin:
                return True
            # Check date and time and origin and destination
            elif self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest < other._dest:
                return True
            # Otherwise false
            else:
                return False

        # Less than or Equal function
        def __le__(self, other):
            # Check date
            if self._date < other._date:
                return True
            # Check date and time
            elif self._date == other._date and self._time <= other._time:
                return True
            # Check date and time and origin
            elif self._date == other._date and self._time == other._time and self._origin <= other._origin:
                return True
            # Check date and time and origin and destination
            elif self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest <= other._dest:
                return True
            # Otherwise false
            else:
                return False

        # Equal to function
        def __eq__(self, other):
            return self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest == other._dest

        # String function
        def __str__(self):
            return print(f"Flight information: {self._date,' ' + self._time,' ' + self._origin,' TO ' + self._dest}")

    # Query function
    def query(self, key1, key2):
        results = []
        for e in self._table:
            key = e._key
            if key1 <= key <= key2:
                results.append(e._value)
        return results

# Testing class: FlightQuery
if __name__ == "__main__":
    # FlightQuery into a variable
    flightsA = FlightQuery()

    # Passing in new elements into list:
    possibleFlights = [("Cuba", "Florida", 622, 1200, "No.1"),
                       ("Cuba", "Florida", 622, 1300, "No.2"),
                       ("Cuba", "Florida", 622, 1500, "No.3"),
                       ("Cuba", "Florida", 622, 1800, "No.4"),
                       ("Miami", "Paris", 777, 1200, "No.5"),
                       ("Miami", "Paris", 777, 1840, "No.6"),
                       ("Cuba", "Cancun", 198, 1100, "No.7"),
                       ("Cuba", "Cancun", 198, 1700, "No.8")]

    # Printing total number of flights
    # Key = origin, destination, date, time
    for element in possibleFlights:
        key = flightsA.Key(element[0], element[1], element[2], element[3])
        flightNum = element[4]
        flightsA[key] = flightNum
    print("\nTotal number of flights: ", len(flightsA))

    print("--------"*5)
    # User 1 query: Cuba to Florida
    print("User 1")
    print("\nFlights from Cuba to Florida between 11:00 and 16:00:")
    key1 = flightsA.Key("Cuba", "Florida", 622, 1100)
    key2 = flightsA.Key("Cuba", "Florida", 622, 1600)
    flights = flightsA.query(key1, key2)
    for f in flights:
        print(f)

    print("--------"*5)
    # User 2 query: Miami to Paris
    print("User 2")
    print("\nFlights from Miami to Paris between 18:00 and 22:00:")
    key1 = flightsA.Key("Miami", "Paris", 198, 1600)
    key2 = flightsA.Key("Miami", "Paris", 198, 2000)
    flights = flightsA.query(key1, key2)
    for f in flights:
        print(f)

    print("--------"*5)
    # User 3 query: Cuba to Cancun
    print("User 3")
    print("\nFlights from Cuba to Cancun between 16:00 and 20:00:")
    key1 = flightsA.Key("Cuba", "Cancun", 777, 1800)
    key2 = flightsA.Key("Cuba", "Cancun", 777, 2200)
    flights = flightsA.query(key1, key2)
    for f in flights:
        print(f)

print("\n")
# User Interface
if __name__ == "__main__":
    # FlightQuery into a variable
    flightsA = FlightQuery()

    def get_user_input():
        origin = input("Departing from: ")
        dest = input("Flying to: ")
        date = int(input("Date (DD:MM): "))
        time = int(input("Departure time (HH:MM): "))

        return origin, dest, date, time

    print("Welcome to Expandia!")
    print("--------"*5)
    possibleFlights = [("Cuba", "Florida", 622, 1200, "No.1"),
                       ("Cuba", "Florida", 622, 1300, "No.2"),
                       ("Cuba", "Florida", 622, 1500, "No.3"),
                       ("Cuba", "Florida", 622, 1800, "No.4"),
                       ("Miami", "Paris", 777, 1200, "No.5"),
                       ("Miami", "Paris", 777, 1840, "No.6"),
                       ("Cuba", "Cancun", 198, 1100, "No.7"),
                       ("Cuba", "Cancun", 198, 1700, "No.8")]
    print("The current flights available are: ", len(possibleFlights))
    print("--------"*5)

    for flight in possibleFlights:
        print(flight)

    # Key = origin, dest, date, time
    for element in possibleFlights:
        key = flightsA.Key(element[0], element[1], element[2], element[3])
        flightNum = element[4]
        flightsA[key] = flightNum

    while True:
        print("Enter flight details below")
        origin, dest, date, time = get_user_input()
        key1 = flightsA.Key(origin, dest, date, time)
        key2 = flightsA.Key(origin, dest, date, time)
        results = flightsA.query(key1, key2)

        if results:
            print("Flights found:")
            for flight in results:
                print(flight)
        else:
            print("No flights found for the specified criteria.")

        continue_query = input("Keep searching? (y/n): ")
        if continue_query.lower() != "y":
            break
        else:
            print("The current flights available are: ", len(possibleFlights))
            print("--------" * 5)

            for flight in possibleFlights:
                print(flight)

    print("Thanks for using Expandia. See you next time!")



