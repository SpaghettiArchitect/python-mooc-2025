def even_numbers(numbers: list[int]) -> list[int]:
    new_numbers = []
    for number in numbers:
        if number % 2 == 0:
            new_numbers.append(number)
    return new_numbers


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
