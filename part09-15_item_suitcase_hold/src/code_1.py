class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() > self.__max_weight:
            return

        self.__items.append(item)

    def __str__(self):
        total_items = len(self.__items)
        if total_items != 1:
            return f"{total_items} items ({self.weight()} kg)"

        return f"{total_items} item ({self.weight()} kg)"

    def print_items(self):

        for item in self.__items:
            print(item)

    def weight(self):
        total_weight = 0

        for item in self.__items:
            total_weight += item.weight()

        return total_weight

    def heaviest_item(self):
        if not self.__items:
            return None

        heaviest = None

        for item in self.__items:

            if heaviest is None or item.weight() > heaviest.weight():
                heaviest = item

        return heaviest


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__weight = 0
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() > self.__max_weight:
            return

        self.__suitcases.append(suitcase)
        self.__weight += suitcase.weight()

    def __str__(self):
        correct_gramar = (
            f"{len(self.__suitcases)} suitcases"
            if len(self.__suitcases) != 1
            else "1 suitcase"
        )
        return f"{correct_gramar}, space for {self.__max_weight - self.__weight} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
