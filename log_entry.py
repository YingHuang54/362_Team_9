import datetime as dt

class LogEntry:
    """
    A class to represent a single log entry. 
    Comparison between instances is limited to their year, month, day, hour, and minute.
    Default format for timestamp's string representation and input are stored in static variables: 
    DATE_FORMAT = "%m/%d/%Y",
    TIME_FORMAT = "%H:%M",
    FORMAT_STR = DATE_FORMAT + ' ' + TIME_FORMAT.

    Static Methods:
        to_str(timestamp_str : str): timestamp to its string representation.
        create_timestamp(timestamp_str : str): string representation to timestamp.

    Attributes:
        timestamp(datetime.datetime): represent the date and time
        drivetime(float): represent the driving time
        resttime(float): represent the resting time
    """

    DATE_FORMAT = "%m/%d/%Y"
    TIME_FORMAT = "%H:%M"
    FORMAT_STR = "%m/%d/%Y %H:%M"

    def __init__(self, timestamp = dt.datetime.now(), drivetime = float(0), resttime = float(0)):
        """
        Constructor of the entry, set to the attribute directly.
        Args: 
            timestamp is an datetime object.
            drivetime is a float (Default: 0.0)
            resttime is a float (Default: 0.0)
        """
        self.timestamp = timestamp
        self.drivetime = float(drivetime)
        self.resttime = float(resttime)

    "Instance Methods"
    def get_timestamp(self):
        """get the datetime.datetime object attribute"""
        return self.timestamp
    def get_drivetime(self):
        """get the drivetime attribute value in floate"""
        return self.drivetime
    def get_resttime(self):
        """get the restime attribute value in floate"""
        return self.resttime
    
    def get_time_str(self):
        """
        Return a string of the time of the entry in the format TIME_FORMAT
        """
        return self.timestamp.strftime(self.TIME_FORMAT)
    
    def get_date_str(self):
        """
        Return a string of the time of the entry in the format DATE_FORMAT
        """
        return self.timestamp.strftime(self.DATE_FORMAT)
    
    def get_timestamp_str(self):
        """
        return a string representation of the entry's attribute timestamp according to the FORMAT_STR.
        """
        return self.timestamp.strftime(LogEntry.FORMAT_STR)

    def set_timestamp(self, timestamp_str : str):
        """
        change the timestamp attribute's date with date/date_str and its time with time_str.
        Args:
        date is a date object used to set the timestamp.
        time_str is a string represent the time to set should be in the format hr:min (24hour).
        """
        self.timestamp = LogEntry.create_timestamp(timestamp_str)
    
    
    "Overload operators"
    def __lt__(self, b):
        return self.get_timestamp_str() < b.get_timestamp_str()
    def __le__(self, b):
        return self.get_timestamp_str() <= b.get_timestamp_str()
    def __eq__(self, b):
        return self.get_timestamp_str() == b.get_timestamp_str()
    def __ne__(self, b):
        return self.get_timestamp_str() != b.get_timestamp_str()
    def __ge__(self, b):
        return self.get_timestamp_str() >= b.get_timestamp_str()
    def __gt__(self, b):
        return self.get_timestamp_str() > b.get_timestamp_str()
    def __str__(self):
        return self.get_timestamp_str()
    
    "Static Methods"
    def to_str(timestamp : dt.datetime):
        """
        Return a string representation of the timestamp in the format defined by LogEntry
        """
        return timestamp.strftime(LogEntry.FORMAT_STR)
    
    def create_timestamp(timestamp_str : str):
        """
        Use the string to create a datetime object according to LogEntry's format.
        default FORMAT_STR = "%m/%d/%Y %H:%M".
        """
        return dt.datetime.strptime(timestamp_str.strip(), LogEntry.FORMAT_STR)
    
    def from_date_and_time(date : dt.date, time_str="00:00"):
        """Return a log entry object by combining date (datetime.date or datetime.datetime instance) 
        and the a string time_str representing the time (default to "00:00")"""
        hour_min = time_str.strip().split(":")
        time = dt.time(int(hour_min[0]), int(hour_min[1]))
        return dt.datetime.combine(date, time)
    
# e = LogEntry(dt.datetime.now(), 10, 12)
# print(e)
# date = dt.date(2024,12,31)
# print(LogEntry.from_date_and_time(date, "12:53"))