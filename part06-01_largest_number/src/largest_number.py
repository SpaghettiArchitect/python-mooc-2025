def largest() -> int:
    with open("numbers.txt") as file:
        largest = 0
        for line in file:
            number = int(line.replace("\n", ""))
            if number > largest:
                largest = number

    return largest


# print(largest())
