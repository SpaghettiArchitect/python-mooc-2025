def filter_solutions() -> None:
    solutions = read_solutions("solutions.csv")
    correct_solutions = []
    incorrect_solutions = []
    for solution in solutions:
        operation = solution[1]
        answer = solution[2]
        if check_solution(operation, answer):
            correct_solutions.append(solution)
        else:
            incorrect_solutions.append(solution)

    save_solution_csv("correct.csv", correct_solutions)
    save_solution_csv("incorrect.csv", incorrect_solutions)


def read_solutions(filename: str) -> list:
    solutions = []
    with open(filename) as file:
        for solution in file:
            solution = solution.strip().split(";")
            name, operation, answer = solution
            operation = operation_to_tuple(operation)
            answer = int(answer)
            solutions.append((name, operation, answer))
    return solutions


def operation_to_tuple(operation: str) -> tuple[int, str, int]:
    if operation.find("+") != -1:
        i = operation.find("+")
        operand1 = int(operation[:i])
        operand2 = int(operation[i + 1 :])
        symbol = "+"
    else:
        i = operation.find("-")
        operand1 = int(operation[:i])
        operand2 = int(operation[i + 1 :])
        symbol = "-"

    return (operand1, symbol, operand2)


def check_solution(operation: tuple[int, str, int], answer: int) -> bool:
    if operation[1] == "+":
        return operation[0] + operation[2] == answer
    else:
        return operation[0] - operation[2] == answer


def save_solution_csv(filename: str, solutions: list[tuple[str, tuple, int]]) -> None:
    with open(filename, "w") as file:
        for solution in solutions:
            name = solution[0]
            answer = solution[2]
            operation = ""
            for item in solution[1]:
                operation += str(item)
            line = f"{name};{operation};{answer}\n"
            file.write(line)


# filter_solutions()
