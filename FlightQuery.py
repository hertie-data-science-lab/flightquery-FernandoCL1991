from SortedTableMap import *
class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    # Class Key which is defined by four arguments: origin, dest, date, time
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        # Initializing instance variables for each Key
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        # Defining the less than method for the Key class to define order of keys in SortedTableMap.
        def __lt__(self, other):
            # These lines implement the less-than method by comparing the origin airport, destination airport,
            # date, and time of each Key object with another Key object.
            # If all of these attributes are equal, then the two Key objects are considered equal.
            if self._origin < other._origin:
                return True
            elif self._origin == other._origin and self._dest < other._dest:
                return True
            elif self._origin == other._origin and self._dest == other._dest and self._date < other._date:
                return True
            elif self._origin == other._origin and self._dest == other._dest and self._date == other._date and self._time < other._time:
                return True
            else:
                return False

    # Defining query method.
    # Taking two arguments for which to represent the range of flights that the method should return.
    def query(self, k1, k2):
        result = []
        for key in self._table:
            if key._origin == k1[0] and key._dest == k1[1]:
                if k1[2:] <= (key._date, key._time) < k2[2:]:
                    result.append(key)
            elif key._origin > k1[0] and key._dest >= k1[1]:
                break
        return result
