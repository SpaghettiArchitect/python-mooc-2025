def store_personal_data(person: tuple) -> None:
    with open("people.csv", "a") as file:
        name = person[0]
        age = person[1]
        height = person[2]
        file.write(f"{name};{age};{height}\n")
