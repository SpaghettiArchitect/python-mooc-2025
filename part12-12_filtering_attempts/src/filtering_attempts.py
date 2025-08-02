class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )


def accepted(attempts: list):
    return list(filter(lambda attempt: attempt.grade >= 1, attempts))


def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda attempt: attempt.grade == 3, attempts))


def passed_students(attempts: list, course: str):
    course_matches = filter(
        lambda attempt: attempt.course_name == course and attempt.grade > 0, attempts
    )
    names_of_students = map(lambda course: course.student_name, course_matches)
    return sorted(list(names_of_students))


if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

    for attempt in accepted([s1, s2, s3]):
        print(attempt)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
