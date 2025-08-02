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


class AppInterface:
    def __init__(self, storage: OrderBook):
        self.__storage = storage

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ").split()

        try:
            programmer = programmer_and_workload[0]
            workload = int(programmer_and_workload[1])
        except (ValueError, IndexError):
            print("erroneous input")
            return

        self.__storage.add_order(description, programmer, workload)
        print("added!")

    def list_finished(self):
        if finished := self.__storage.finished_orders():
            for task in finished:
                print(task)
        else:
            print("no finished tasks")

    def list_unfinished(self):
        if unfinished := self.__storage.unfinished_orders():
            for task in unfinished:
                print(task)
        else:
            print("no unfinished tasks")

    def mark_task_finished(self):
        try:
            task_id = int(input("id: "))
            self.__storage.mark_finished(task_id)
        except ValueError:
            print("erroneous input")
            return

        print("marked as finished")

    def list_programmers(self):
        programmers = self.__storage.programmers()
        for programmer in programmers:
            print(programmer)

    def get_programmer_status(self):
        programmer = input("programmer: ")

        try:
            status = self.__storage.status_of_programmer(programmer)
        except ValueError:
            print("erroneous input")
            return

        tasks = f"tasks: finished {status[0]} not finished {status[1]}"
        hours = f"hours: done {status[2]} scheduled {status[3]}"

        print(f"{tasks}, {hours}")

    def run(self):

        self.help()

        while True:
            print()

            command = int(input("command: "))

            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished()
            elif command == 3:
                self.list_unfinished()
            elif command == 4:
                self.mark_task_finished()
            elif command == 5:
                self.list_programmers()
            elif command == 6:
                self.get_programmer_status()
            else:
                self.help()


order_book = OrderBook()
app = AppInterface(order_book)

app.run()
