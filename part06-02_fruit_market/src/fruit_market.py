def read_fruits() -> dict:
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line_data = line.replace("\n", "")
            fruit, price = line_data.split(";")
            price = float(price)
            fruits[fruit] = price

    return fruits


# print(read_fruits())
