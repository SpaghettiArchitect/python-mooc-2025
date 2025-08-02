# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number: int):
        self.sum += number
        self.numbers += 1

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum

    def average(self):
        if self.sum == 0:
            return 0
        return self.sum / self.numbers


def main() -> None:
    print("Please type in integer numbers:")

    stats = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    while True:

        number = int(input())

        if number == -1:
            break
        elif number % 2 == 0:
            stats_even.add_number(number)
        else:
            stats_odd.add_number(number)

        stats.add_number(number)

    print(f"Sum of numbers: {stats.get_sum()}")
    print(f"Mean of numbers: {stats.average()}")
    print(f"Sum of even numbers: {stats_even.get_sum()}")
    print(f"Sum of odd numbers: {stats_odd.get_sum()}")


main()
