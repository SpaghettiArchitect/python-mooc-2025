from datetime import datetime, timedelta


def main() -> None:
    filename = input("Filename: ")
    start_date = input("Starting date: ")
    total_days = int(input("How many days: "))

    start_date = datetime.strptime(start_date, "%d.%m.%Y")

    print("Please type in screen time in minutes on each day (TV computer mobile):")

    all_screen_times = {}
    tmp_date = start_date
    for _ in range(total_days):
        current_day = tmp_date.strftime(f"%d.%m.%Y")
        screen_time = input(f"Screen time {current_day}: ")
        tv, computer, mobile = screen_time.split(" ")
        all_screen_times[current_day] = (int(tv), int(computer), int(mobile))
        tmp_date += timedelta(days=1)

    save_data(filename, all_screen_times, start_date, total_days)
    print(f"Data stored in file {filename}")


def save_data(filename: str, data: dict, start_date: datetime, total_days: int):
    total_minutes = 0
    for day in data.values():
        total_minutes += sum(day)

    avg_minutes = total_minutes / total_days

    end_date = start_date + timedelta(days=(total_days - 1))

    str_start_date = start_date.strftime("%d.%m.%Y")
    str_end_date = end_date.strftime("%d.%m.%Y")

    with open(filename, "w") as file:
        file.write(f"Time period: {str_start_date}-{str_end_date}\n")
        file.write(f"Total minutes: {total_minutes}\n")
        file.write(f"Average minutes: {avg_minutes:.1f}\n")
        for date, minutes in data.items():
            file.write(f"{date}: {minutes[0]}/{minutes[1]}/{minutes[2]}\n")


main()
