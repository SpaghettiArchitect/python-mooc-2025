def strings_to_ints(numbers: list[str]) -> list[int]:
    new_numbers = []
    for number in numbers:
        new_numbers.append(int(number))

    return new_numbers


def matrix_sum() -> int:
    total_sum = 0
    with open("matrix.txt") as file:
        for line in file:
            data_str = line.replace("\n", "").split(",")
            data_int = strings_to_ints(data_str)
            total_sum += sum(data_int)
    return total_sum


def matrix_max() -> int:
    max_value = 0
    with open("matrix.txt") as file:
        for line in file:
            data_str = line.replace("\n", "").split(",")
            data_int = strings_to_ints(data_str)
            max_value = max(max(data_int), max_value)

    return max_value


def row_sums() -> list[int]:
    result = []
    with open("matrix.txt") as file:
        for line in file:
            data_str = line.replace("\n", "").split(",")
            data_int = strings_to_ints(data_str)
            result.append(sum(data_int))

    return result


# print(row_sums())
