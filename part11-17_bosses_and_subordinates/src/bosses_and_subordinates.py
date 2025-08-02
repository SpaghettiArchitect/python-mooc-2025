class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: "Employee"):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    # Base case: if the employee doesn't have subordinates (empty list)
    if not employee.subordinates:
        return 0

    # Now, if the employee HAS subordinates:
    # The total number of direct subordinates of this employee
    direct_subordinates = len(employee.subordinates)

    # Add all the indirect subordinates of the current employee to the total
    # no matter how many levels deep
    indirect_subordinates = 0
    for subordinate in employee.subordinates:
        indirect_subordinates += count_subordinates(subordinate)

    # Return all the subordinates of the current employee
    return direct_subordinates + indirect_subordinates


if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))  # 5
    print(count_subordinates(t4))  # 3
    print(count_subordinates(t5))  # 0
