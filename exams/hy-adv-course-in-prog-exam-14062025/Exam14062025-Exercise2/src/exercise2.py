class Car:
    current_year = 0

    def __init__(self, brand: str, purchase_year: int, purchase_price: int):
        self.brand = brand
        self.purchase_year = purchase_year
        self.purchase_price = purchase_price

        if purchase_year > Car.current_year:
            Car.current_year = purchase_year

        # Keep track of the total kilometers driven and the costs.
        self.__total_kilometers = 0
        self.__total_costs = 0

    def set_year(self, new_year: int):
        if new_year > Car.current_year:
            Car.current_year = new_year

    def drive(self, distance_driven: int, cost_per_kilometer: float):
        self.__total_kilometers += distance_driven
        self.__total_costs += distance_driven * cost_per_kilometer

    def add_expense(self, expense: int):
        self.__total_costs += expense

    def distance_driven_by_car(self):
        return self.__total_kilometers

    def current_value(self):
        years_passed = Car.current_year - self.purchase_year
        current_value = self.purchase_price
        for year in range(years_passed):
            current_value = current_value - (current_value * 0.15)
        return int(current_value)

    def cost_per_kilometer(self):
        car_depreciation = self.purchase_price - self.current_value()
        total_costs = self.__total_costs + car_depreciation
        return total_costs / self.__total_kilometers

    def __str__(self):
        car_str = f"{self.brand}:"
        car_str += f" purchase year {self.purchase_year},"
        car_str += f" value {self.current_value()}"
        return car_str
