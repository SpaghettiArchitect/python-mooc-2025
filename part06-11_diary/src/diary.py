def main():
    filename = "diary.txt"
    diary = read_diary(filename)

    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        command = int(input("Function: "))
        if command == 0:
            print("Bye now!")
            break
        elif command == 1:
            entry = input("Diary entry: ")
            write_to_diary(filename, entry)
            diary.append(entry)
            print("Diary saved")
            print()
        elif command == 2:
            print("Entries:")
            for entry in diary:
                print(entry)


def write_to_diary(filename: str, entry: str) -> None:
    with open(filename, "a") as diary:
        diary.write(f"{entry}\n")


def read_diary(filename: str) -> list[str]:
    all_entries = []
    with open(filename) as diary:
        for entry in diary:
            all_entries.append(entry.strip())

    return all_entries


main()
