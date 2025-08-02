def remove_smallest(numbers: list[int]) -> None:
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    numbers.remove(smallest)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
