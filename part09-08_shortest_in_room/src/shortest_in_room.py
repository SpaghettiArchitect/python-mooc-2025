# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if len(self.people) == 0:
            return True
        return False

    def print_contents(self):
        total_height = 0
        list_of_people = ""

        for person in self.people:
            total_height += person.height
            list_of_people += f"{person.name} ({person.height} cm)\n"

        list_of_people = list_of_people.strip()

        print(
            f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm"
        )
        print(list_of_people)

    def shortest(self):
        if len(self.people) == 0:
            return None

        shortest = self.people[0]
        for person in self.people:
            if person.height < shortest.height:
                shortest = person

        return shortest

    def remove_shortest(self):
        if len(self.people) == 0:
            return None

        shortest = self.shortest()
        index = self.people.index(shortest)

        return self.people.pop(index)


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
