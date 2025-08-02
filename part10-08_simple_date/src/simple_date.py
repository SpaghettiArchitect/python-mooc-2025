class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __to_days(self):
        days = self.__day + (self.__month * 30) + (12 * 30 * self.__year)
        return days

    @classmethod
    def __days_to_date(self, days: int):
        years = days // (12 * 30)
        days -= years * 12 * 30
        months = days // 30
        days -= months * 30

        return SimpleDate(days, months, years)

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, other: "SimpleDate"):
        return (
            self.__day == other.__day
            and self.__month == other.__month
            and self.__year == other.__year
        )

    def __ne__(self, other: "SimpleDate"):
        return not self == other

    def __lt__(self, other: "SimpleDate"):
        return self.__to_days() < other.__to_days()

    def __gt__(self, other: "SimpleDate"):
        return self.__to_days() > other.__to_days()

    def __add__(self, days: int):
        return SimpleDate.__days_to_date(self.__to_days() + days)

    def __sub__(self, other: "SimpleDate"):
        return abs(self.__to_days() - other.__to_days())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
