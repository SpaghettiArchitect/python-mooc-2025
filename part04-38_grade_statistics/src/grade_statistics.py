def main() -> None:
    alumni = []
    while True:
        student_points = input("Exam points and exercises completed: ")
        if student_points == "":
            break
        # [exam_points, total_exercises]
        tmp_student = transform_to_ints(student_points)
        # [exam_points, exercise_points]
        tmp_student[1] = get_exercise_points(tmp_student[1])
        tmp_student = get_total_grade_and_points(tmp_student[0], tmp_student[1])
        alumni.append(tmp_student)

    print(get_statistics(alumni))


def transform_to_ints(input: str) -> list[int]:
    """Trasforms a string with two integers into a list of two integers."""
    list_int = []
    list_str = input.split()
    list_int.append(int(list_str[0]))
    list_int.append(int(list_str[1]))

    return list_int


def get_exercise_points(num_of_exercises: int) -> int:
    """
    Calculates the total number of exercise points.

    Return: a point for each 10 exercises completed
    """
    return num_of_exercises // 10


def get_total_grade_and_points(exam_points: int, exercise_points: int) -> list[int]:
    """
    Calculates the grade and the total points of the current alumni.

    Input: total exam points and exercise points
    Return: list[grade, total_points]
    """
    grade_and_points = []
    total_points = exam_points + exercise_points
    if exam_points < 10 or 0 <= total_points <= 14:
        grade_and_points = [0, total_points]
    elif 15 <= total_points <= 17:
        grade_and_points = [1, total_points]
    elif 18 <= total_points <= 20:
        grade_and_points = [2, total_points]
    elif 21 <= total_points <= 23:
        grade_and_points = [3, total_points]
    elif 24 <= total_points <= 27:
        grade_and_points = [4, total_points]
    elif 28 <= total_points <= 30:
        grade_and_points = [5, total_points]

    return grade_and_points


def calc_points_average(total_alumni: list[list[int]]) -> float:
    number_of_alumni = 0
    total_points = 0
    for alumni in total_alumni:
        number_of_alumni += 1
        # alumni -> [grade, points] we just want the points
        total_points += alumni[1]

    return total_points / number_of_alumni


def calc_pass_percentage(total_alumni: list[list[int]]) -> float:
    number_of_alumni = 0
    pass_alumni = 0
    for alumni in total_alumni:
        # alumni -> [grade, points] we just want the grade
        if alumni[0] != 0:
            pass_alumni += 1
        number_of_alumni += 1

    return (pass_alumni / number_of_alumni) * 100


def format_grade_distribution(total_alumni: list[list[int]]) -> str:
    # Extract only the grades
    grades = [0, 0, 0, 0, 0, 0]
    for student in total_alumni:
        # student -> [grade, points] we just want the grade
        grades[student[0]] += 1

    result = ""
    for grade in range(5, -1, -1):
        if grades[grade] != 0:
            result += f"  {grade}: {'*' * grades[grade]}\n"
        else:
            result += f"  {grade}:\n"

    return result.rstrip("\n")


def get_statistics(total_alumni: list[list[int]]) -> str:
    result = "Statistics:\n"
    result += f"Points average: {calc_points_average(total_alumni):.1f}\n"
    result += f"Pass percentage: {calc_pass_percentage(total_alumni):.1f}\n"
    result += f"Grade distribution:\n{format_grade_distribution(total_alumni)}"
    return result


main()
