def main() -> None:
    if True:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_data = "exam_points1.csv"

    students = {}
    with open(student_info) as student_file:
        for line in student_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity, first, last = data
            students[identity] = f"{first} {last}"

    exercises = {}
    with open(exercise_data) as exercise_file:
        for line in exercise_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity = data[0]
            grades = []
            for grade in data[1:]:
                grades.append(int(grade))

            exercises[identity] = grades

    exams = {}
    with open(exam_data) as exam_file:
        for line in exam_file:
            data = line.strip().split(";")
            if data[0] == "id":
                continue
            identity = data[0]
            points = []
            for point in data[1:]:
                points.append(int(point))
            exams[identity] = points

    # print_total_exercises(students, exercises)
    # print_grades(students, exercises, exams)
    print_statistics(students, exercises, exams)


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
    print(
        f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
    )

    for id, name in students.items():
        if id in exercises:
            exec_nbr = sum(exercises[id])
            exec_pts = exec_nbr // 4
        if id in exams:
            exm_pts = sum(exams[id])
        tot_pts = exec_pts + exm_pts
        grade = get_grade(tot_pts)

        print(
            f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}"
        )


main()
