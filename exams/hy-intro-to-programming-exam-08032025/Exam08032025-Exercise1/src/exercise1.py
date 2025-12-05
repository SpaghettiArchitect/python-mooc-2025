def main() -> None:
    numbers = get_numbers()

    biggest = max(numbers)
    smallest = min(numbers)
    num_of_numbers = len(numbers)
    total = sum(numbers)

    most_repeated = 0
    max_repetitions = 0
    for number in numbers:
        if numbers.count(number) > max_repetitions:
            max_repetitions = numbers.count(number)
            most_repeated = number

    print(f"Biggest: {biggest}")
    print(f"Smallest: {smallest}")
    print(f"Number of numbers: {num_of_numbers}")
    print(f"Sum: {total}")
    print(f"Most repeated: {most_repeated}")


def get_numbers() -> list:
    numbers = []
    while True:
        number = int(input("Type in a number: "))
        if number == 0:
            break
        numbers.append(number)

    return numbers


main()
