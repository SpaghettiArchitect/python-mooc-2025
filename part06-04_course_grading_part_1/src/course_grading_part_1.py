def main() -> None:
    if True:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"

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

    for id, name in students.items():
        if id in exercises:
            print(f"{name} {sum(exercises[id])}")


main()
