# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str):
        self.__name = name
        self.__grade = 0
        self.__credits = 0

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade: int):
        if grade > self.__grade and not grade > 5:
            self.__grade = grade

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits: int):
        if credits > 0:
            self.__credits = credits


class Studies:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        self.__courses[name].grade = grade
        self.__courses[name].credits = credits

    def get_course(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]

    def get_completed_courses(self):
        return len(self.__courses)

    def get_total_grades(self):
        total_grades = 0
        for course in self.__courses.values():
            total_grades += course.grade
        return total_grades

    def get_total_credits(self):
        total_credits = 0
        for course in self.__courses.values():
            total_credits += course.credits
        return total_credits

    def get_mean(self):
        total_grades = self.get_total_grades()
        total_courses = self.get_completed_courses()
        if total_courses == 0:
            return None
        return total_grades / total_courses

    def get_grade_distribution(self):
        grade_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for course in self.__courses.values():
            grade_distribution[course.grade] += 1
        return grade_distribution


class AppInterface:
    def __init__(self):
        self.__studies = Studies()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__studies.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__studies.get_course(name)
        if course:
            print(course)
        else:
            print("no entry for this course")

    def print_statistics(self):
        completed = self.__studies.get_completed_courses()
        credits = self.__studies.get_total_credits()
        mean = round(self.__studies.get_mean(), 1)

        print(f"{completed} completed courses, a total of {credits} credits")
        print(f"mean {mean}")

        print("grade distribution")
        grades = self.__studies.get_grade_distribution()
        for grade in range(5, 0, -1):
            padding = " " if grades[grade] != 0 else ""
            stars = grades[grade] * "x"
            print(f"{grade}:{padding + stars}")

    def execute(self):
        self.help()
        while True:
            command = input("\ncommand: ")

            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.print_statistics()
            else:
                self.help()


def main():
    program = AppInterface()
    program.execute()


main()
