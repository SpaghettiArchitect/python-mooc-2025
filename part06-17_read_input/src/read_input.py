def main() -> None:
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)


def read_input(instruction: str, lower: int, upper: int) -> int:
    while True:
        try:
            number_str = input(instruction)
            number = int(number_str)
            if lower <= number <= upper:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {lower} and {upper}")


# main()
