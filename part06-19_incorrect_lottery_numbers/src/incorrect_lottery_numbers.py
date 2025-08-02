def filter_incorrect() -> None:
    correct_lottery = []
    with open("lottery_numbers.csv") as lottery_file:
        for line_data in lottery_file:
            tmp_week, tmp_numbers = line_data.strip().split(";")
            tmp_numbers = tmp_numbers.split(",")
            tmp_week_numbers = []
            try:
                # The week number is incorrect
                int(tmp_week.split(" ")[1])

                # Too few numbers
                if len(tmp_numbers) != 7:
                    raise ValueError("Too few numbers")

                for number in tmp_numbers:
                    # One or more numbers are not correct
                    number = int(number)
                    # The numbers are too small or large
                    if not (1 <= number <= 39):
                        raise ValueError("The numbers are too small or large")
                    # The same number appears twice
                    if number in tmp_week_numbers:
                        raise ValueError("The same number appears twice")

                    tmp_week_numbers.append(number)

            except ValueError:
                continue

            # If the data is correct, add it to list
            correct_lottery.append(line_data)

    # Line correct lines to file
    with open("correct_numbers.csv", "w") as file:
        for line in correct_lottery:
            file.write(line)


# filter_incorrect()
