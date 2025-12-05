class Question:
    def __init__(self, question: str, maximum_points: int):
        self.__question = question
        self.__maximum_points = maximum_points

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def maximum_points(self):
        return self.__maximum_points

    @maximum_points.setter
    def maximum_points(self, maximum_points: int):
        self.__maximum_points = maximum_points

    def __str__(self):
        return f"{self.__question}, {self.__maximum_points} points"


class Exam:
    def __init__(self, subject: str, date: str):
        self.subject = subject
        self.date = date
        self.__questions = []

    def add_question(self, question: Question):
        self.__questions.append(question)

    def print_questions(self):
        print(f"Exam on {self.subject}, questions:")
        for question in self.__questions:
            print(question)

    def total_points(self):
        total = 0
        for question in self.__questions:
            total += question.maximum_points
        return total
