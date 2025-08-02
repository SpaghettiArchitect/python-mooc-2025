import csv
from datetime import datetime, timedelta


def main() -> None:
    all_cheaters = cheaters()
    print(all_cheaters)


def cheaters():
    students = load_students_and_sub("start_times.csv", "submissions.csv")

    cheaters = []
    for name, student in students.items():
        if student["end_time"] - student["start_time"] > timedelta(hours=3):
            cheaters.append(name)

    return cheaters


def load_students_and_sub(start_times: str, submissions: str) -> dict:
    students_start = load_start_times(start_times)
    load_submissions(submissions, students_start)
    return students_start


def load_start_times(filename: str) -> dict[dict]:
    start_times = {}
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file, ["name", "start_time"], delimiter=";")
        for line in reader:
            current_time = datetime.strptime(line["start_time"], "%H:%M")
            start_times[line["name"]] = {"start_time": current_time}

    return start_times


def load_submissions(filename: str, students: dict[dict]) -> None:
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(
            csv_file, ["name", "task", "points", "hour"], delimiter=";"
        )
        for line in reader:

            name = line["name"]
            task_number = int(line["task"])
            task_points = int(line["points"])
            time = datetime.strptime(line["hour"], "%H:%M")

            if "tasks" not in students[name] and "end_time" not in students[name]:
                students[name]["tasks"] = {}
                students[name]["end_time"] = time

            if task_number not in students[name]["tasks"]:
                students[name]["tasks"][task_number] = 0

            if (time - students[name]["start_time"]) < timedelta(hours=3):
                students[name]["tasks"][task_number] = max(
                    task_points, students[name]["tasks"][task_number]
                )

            students[name]["end_time"] = max(students[name]["end_time"], time)


# main()
