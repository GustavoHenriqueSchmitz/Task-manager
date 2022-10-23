import datetime
import calendar


class Date:
    def __init__(
        self,
        year=datetime.date.today().strftime("%Y"),
        month=datetime.date.today().strftime("%m"),
        day=datetime.date.today().strftime("%d"),
        hour=datetime.datetime.now().strftime("%H"),
        minute=datetime.datetime.now().strftime("%M"),
        second=datetime.datetime.now().strftime("%S"),
    ):

        """
        :param year: The year, by default is the current year
        :param month: The month, by default is the current month
        :param day: The day, by default is the current day
        :param hour: The hour, by default is the current hour
        :param minute: The minute, by default is the current minute
        :param second: The second, by default is the current second
        """

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.__date = f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"
        self.__dateSeparated = {
            "year": f"{self.year}",
            "month": f"{self.month}",
            "day": f"{self.day}",
            "hour": f"{self.hour}",
            "minute": f"{self.minute}",
            "second": f"{self.second}",
        }

    def DateSeparated(self):

        """
        This method works against the created object

        :return: Return a dictionary with the separated date
        """

        return self.__dateSeparated

    def Date(self):

        """
        This method works against the created object

        :return: Return the date
        """

        return self.__date

    def DateByType(self, dateType=str):

        """
        This method works against the created object

        :param dateType: Type
        Digit:
        y -> For return the year
        m -> For return the month
        d -> For return the day
        h -> For return the hour
        m -> For return the minute
        s -> For return the second

        :return: Return the selected type
        """

        if dateType == "y":
            return self.__dateSeparated["year"]
        elif dateType == "m":
            return self.__dateSeparated["month"]
        elif dateType == "d":
            return self.__dateSeparated["day"]
        elif dateType == "h":
            return self.__dateSeparated["hour"]
        elif dateType == "m":
            return self.__dateSeparated["minute"]
        elif dateType == "s":
            return self.__dateSeparated["second"]
        else:
            print(
                f"\033[31mThe digited type is invalid:\033[1;31m\n"
                f"Digit\n"
                f"\033[32m -> y -> For return the year\n"
                f"\033[32m -> m -> For return the month\n"
                f"\033[32m -> d -> For return the day\n"
                f"\033[32m -> h -> For return the hour\n"
                f"\033[32m -> m -> For return the minute\n"
                f"\033[32m -> s -> For return the second\n\033[m"
            )

    @staticmethod
    def numberDaysMonth(year, month):

        """
        :param year: The year
        :param month: The month
        :return: Return the days quantity of the month
        """

        monthDays = calendar.monthrange(year, month)
        return monthDays[1]
