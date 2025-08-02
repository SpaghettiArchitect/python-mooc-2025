import urllib.request
import json


def main() -> None:
    print(retrieve_course("docker2019"))


def retrieve_all() -> list:
    response = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    )
    data = response.read()
    courses = json.loads(data)

    result = []
    for course in courses:
        if course["enabled"] == True:
            result.append(
                (
                    course["fullName"],
                    course["name"],
                    course["year"],
                    sum(course["exercises"]),
                )
            )

    return result


def retrieve_course(course_name: str) -> dict:
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(url)
    data = response.read()
    course_data = json.loads(data)

    weeks = len(course_data)
    students = 0
    hours = 0
    exercises = 0
    for week in course_data.values():
        if week["students"] > students:
            students = week["students"]
        hours += week["hour_total"]
        exercises += week["exercise_total"]
    hours_average = hours // students
    exercises_average = exercises // students

    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average,
    }


# main()
