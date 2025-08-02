from string import ascii_uppercase


def main() -> None:
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)


def run(program: list) -> list:
    # Initialize all variables to 0
    variables = {}
    for variable in ascii_uppercase:
        variables[variable] = 0

    # First past of the program: register all location indexes
    locations = {}
    for index, instruction in enumerate(program):
        if ":" in instruction:
            location = instruction.replace(":", "")
            locations[location] = index

    # Second past of the program: execute instructions in order
    output = []
    index = 0
    while index < len(program):
        line = program[index].split()

        # Name of the instrution
        instruction = line[0]

        # Get the variable and value we are working on
        variable, value = get_var_and_value(instruction, line, variables)

        # Ignore location definitions, since we already register them
        if ":" in line:
            index += 1

        # Implements print funtionality
        elif instruction == "PRINT":
            output.append(value)
            index += 1

        # Implements assignation, addition, substraction and multiplication
        elif instruction in ["MOV", "ADD", "SUB", "MUL"]:
            do_basic_operation(instruction, variable, value, variables)
            index += 1

        # Implements loops
        elif instruction == "JUMP":
            location = line[1]
            index = locations[location]

        # Implements conditionals
        elif instruction == "IF":
            conditional = evaluate_condition(line[1:4], variables)
            location = line[-1]
            if conditional:
                index = locations[location]
            else:
                index += 1

        # Finishes execution
        elif instruction == "END":
            break

        else:
            index += 1

    return output


def get_value(value: str, variables: dict) -> int:
    if value.isalpha():
        return variables[value]
    else:
        return int(value)


def get_var_and_value(kwd: str, line: str, variables: dict) -> tuple:
    value = 0
    variable = ""
    if kwd == "PRINT":
        value = get_value(line[-1], variables)
    elif kwd in ["MOV", "ADD", "SUB", "MUL"]:
        variable = line[1]
        value = get_value(line[-1], variables)
    return variable, value


def do_basic_operation(kwd: str, variable: str, value: int, variables: dict) -> None:
    if kwd == "MOV":
        variables[variable] = value
    elif kwd == "ADD":
        variables[variable] += value
    elif kwd == "SUB":
        variables[variable] -= value
    elif kwd == "MUL":
        variables[variable] *= value


def evaluate_condition(condition: list, variables: dict) -> bool:
    value1, operand, value2 = condition
    value1 = get_value(value1, variables)
    value2 = get_value(value2, variables)

    if operand == "==":
        return value1 == value2
    elif operand == "!=":
        return value1 != value2
    elif operand == "<":
        return value1 < value2
    elif operand == ">":
        return value1 > value2
    elif operand == "<=":
        return value1 <= value2
    elif operand == ">=":
        return value1 >= value2


# if __name__ == "__main__":
#     main()
