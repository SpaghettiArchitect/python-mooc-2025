def main() -> None:
    if True:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")
        course_info = input("Course information: ")
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_data = "exam_points1.csv"
        course_info = "course1.txt"

    students = load_students(student_info)
    exercises = load_exercises(exercise_data)
    exams = load_exams(exam_data)
    course = load_course_info(course_info)
    results = get_results(students, exercises, exams)

    # print_total_exercises(students, exercises)
    # print_grades(students, exercises, exams)
    # print_statistics(students, exercises, exams)
    write_results_txt(students, exercises, exams, course)
    write_results_csv(results)
    print("Results written to files results.txt and results.csv")


def load_course_info(filename: str) -> tuple[str, int]:
    course = []
    with open(filename) as file:
        for line in file:
            line = line.strip().split(": ")
            course.append(line[1])
    return (course[0], int(course[1]))


def format_course_info(course: tuple[str, int]) -> str:
    course_name = course[0]
    credits = course[1]
    title = f"{course_name}, {credits} credits"
    decoration = "=" * len(title)
    result = f"{title}\n{decoration}"
    return result


def write_results_txt(students: dict, exercises: dict, exams: dict, course: tuple):
    title = format_course_info(course)
    statistics = generate_statistics(students, exercises, exams)
    with open("results.txt", "w") as results:
        results.write(f"{title}\n{statistics}")


def write_results_csv(results: dict) -> None:
    with open("results.csv", "w") as csv:
        for id, result in results.items():
            csv.write(f"{id};{result["name"]};{result["grade"]}\n")


def load_students(filename: str) -> dict:
    students = {}
    with open(filename) as student_file:
        for line in student_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity, first, last = data
            students[identity] = f"{first} {last}"
    return students


def load_exercises(filename: str) -> dict:
    exercises = {}
    with open(filename) as exercise_file:
        for line in exercise_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity = data[0]
            grades = []
            for grade in data[1:]:
                grades.append(int(grade))

            exercises[identity] = grades
    return exercises


def load_exams(filename: str) -> dict:
    exams = {}
    with open(filename) as exam_file:
        for line in exam_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity = data[0]
            points = []
            for point in data[1:]:
                points.append(int(point))
            exams[identity] = points
    return exams


def print_total_exercises(students: dict, exercises: dict) -> None:
    for id, name in students.items():
        if id in exercises:
            print(f"{name} {sum(exercises[id])}")


def print_grades(students: dict, exercises: dict, exams: dict) -> None:
    for id, name in students.items():
        total_points = 0
        if id in exercises:
            total_points += sum(exercises[id]) // 4
        if id in exams:
            total_points += sum(exams[id])
        print(f"{name} {get_grade(total_points)}")


def get_grade(points: int) -> int:
    if 0 <= points <= 14:
        return 0
    elif 15 <= points <= 17:
        return 1
    elif 18 <= points <= 20:
        return 2
    elif 21 <= points <= 23:
        return 3
    elif 24 <= points <= 27:
        return 4
    else:
        return 5


def print_statistics(students: dict, exercises: dict, exams: dict) -> None:
    statistics = generate_statistics(students, exercises, exams)
    print(statistics)


def generate_statistics(students: dict, exercises: dict, exams: dict) -> str:
    statistics = f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"

    for id, name in students.items():
        if id in exercises:
            exec_nbr = sum(exercises[id])
            exec_pts = exec_nbr // 4
        if id in exams:
            exm_pts = sum(exams[id])
        tot_pts = exec_pts + exm_pts
        grade = get_grade(tot_pts)

        statistics += f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n"

    return statistics.strip()


def get_results(students: dict, exercises: dict, exams: dict) -> dict:
    results = {}
    for id, name in students.items():
        if id in exercises:
            exec_nbr = sum(exercises[id])
            exec_pts = exec_nbr // 4
        if id in exams:
            exm_pts = sum(exams[id])
        tot_pts = exec_pts + exm_pts
        grade = get_grade(tot_pts)
        results[id] = {
            "name": name,
            "exec_nbr": exec_nbr,
            "exec_pts": exec_pts,
            "exm_pts": exm_pts,
            "tot_pts": tot_pts,
            "grade": grade,
        }
    return results


main()
