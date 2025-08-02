def main() -> None:
    # Part 1
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
    # Part 2
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")
    # Part 3
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")
    # Part 4
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


def add_student(students: dict, name: str) -> None:
    students[name] = {}


def print_student(students: dict, name: str) -> None:
    # print(students)
    if name in students:
        print(f"{name}:")
        total_courses = len(students[name])
        if total_courses > 0:
            print(f" {total_courses} completed courses:")
            total_grade = 0
            for course, grade in students[name].items():
                print(f"  {course} {grade}")
                total_grade += grade
            average = total_grade / total_courses
            print(f" average grade {average:.1f}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")


def add_course(students: dict, name: str, course: tuple[str, int]) -> None:
    course_name = course[0]
    course_grade = course[1]
    if course_grade > 0:
        student = students[name]
        if course_name in student:
            student[course_name] = max(student[course_name], course_grade)
        else:
            student[course_name] = course_grade


def summary(students: dict) -> None:
    print(f"students {len(students)}")
    max_courses = 0
    max_courses_name = ""
    best_avg = 0
    best_avg_name = ""
    for name in students:
        total_courses = len(students[name])
        if total_courses > max_courses:
            max_courses = total_courses
            max_courses_name = name

        total_grade = 0
        for course_grade in students[name].values():
            total_grade += course_grade

        if total_courses == 0:
            avg_grade = 0
        else:
            avg_grade = total_grade / total_courses

        if avg_grade > best_avg:
            best_avg = avg_grade
            best_avg_name = name

    print(f"most courses completed {max_courses} {max_courses_name}")
    print(f"best average grade {best_avg:.1f} {best_avg_name}")


if __name__ == "__main__":
    main()
