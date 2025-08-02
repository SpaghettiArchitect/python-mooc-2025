from random import sample


def main() -> None:
    for number in lottery_numbers(7, 1, 40):
        print(number)


def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    result = []
    number_pool = list(range(lower, upper + 1))
    result = sample(number_pool, amount)
    result.sort()
    return result


# main()
