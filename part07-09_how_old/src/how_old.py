from datetime import datetime


def main() -> None:
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    birthday = datetime(year, month, day)
    new_millennium = datetime(1999, 12, 31)
    difference = new_millennium - birthday

    if difference.days >= 0:
        print(f"You were {difference.days} days old on the eve of the new millennium.")
    else:
        print("You weren't born yet on the eve of the new millennium.")


main()
