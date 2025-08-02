from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list):
    return reduce(lambda credits, attempt: credits + attempt.credits, attempts, 0)


def sum_of_passed_credits(attempts: list):
    passed_courses = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda credits, attempt: credits + attempt.credits, passed_courses, 0)


def average(attempts: list):
    passed_courses = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    total_of_grades = reduce(
        lambda grades, attempt: grades + attempt.grade, passed_courses, 0
    )
    return total_of_grades / len(passed_courses)


if __name__ == "__main__":
    # Test for the sum of all credits
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    # Test for the sum of passed credits
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    # Test for average grade for passed courses
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
