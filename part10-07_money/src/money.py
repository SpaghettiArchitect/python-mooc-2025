# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __to_cents(self):
        return self.__euros * 100 + self.__cents

    @classmethod
    def __cents_to_money(cls, amount: int):
        euros = amount // 100
        cents = amount % 100
        return Money(euros, cents)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: "Money"):
        return self.__to_cents() == another.__to_cents()

    def __lt__(self, another: "Money"):
        return self.__to_cents() < another.__to_cents()

    def __gt__(self, another: "Money"):
        return self.__to_cents() > another.__to_cents()

    def __ne__(self, another: "Money"):
        return self.__to_cents() != another.__to_cents()

    def __add__(self, another: "Money"):
        result = self.__to_cents() + another.__to_cents()
        return Money.__cents_to_money(result)

    def __sub__(self, another: "Money"):
        result = self.__to_cents() - another.__to_cents()

        if result < 0:
            raise ValueError("A negative result is not allowed")

        return Money.__cents_to_money(result)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1
