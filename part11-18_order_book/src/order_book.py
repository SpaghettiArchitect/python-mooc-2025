class Task:

    __id = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__finished = False
        self.id = Task.__id
        Task.__id += 1

    def is_finished(self):
        return self.__finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self):
        is_finished = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {is_finished}"


class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.__orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__orders

    def programmers(self):
        programmers = [task.programmer for task in self.__orders]
        unique_programmers = list(set(programmers))
        return unique_programmers

    def mark_finished(self, id: int):
        for task in self.__orders:
            if task.id == id:
                task.mark_finished()
                return
        else:
            raise ValueError("No task with the given id")

    def finished_orders(self):
        return [task for task in self.__orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.__orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):

        if programmer not in self.programmers():
            raise ValueError("No programmer with the given name")

        total_finished = 0
        total_unfinished = 0
        workload_finished = 0
        workload_unfinished = 0

        for task in self.__orders:
            if task.programmer == programmer:
                if task.is_finished():
                    total_finished += 1
                    workload_finished += task.workload
                else:
                    total_unfinished += 1
                    workload_unfinished += task.workload

        return (
            total_finished,
            total_unfinished,
            workload_finished,
            workload_unfinished,
        )


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
