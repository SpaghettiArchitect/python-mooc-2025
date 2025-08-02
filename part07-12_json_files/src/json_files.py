import json


def main() -> None:
    print_persons("file3.json")


def print_persons(filename: str) -> None:
    with open(filename) as file:
        data = file.read()

    students = json.loads(data)

    for student in students:
        hobbies = ""
        for hobby in student["hobbies"]:
            hobbies += hobby + ", "
        hobbies = hobbies[:-2]

        print(f"{student['name']} {student['age']} years ({hobbies})")


# main()
