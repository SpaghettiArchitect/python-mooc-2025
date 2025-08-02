def oldest_person(people: list[tuple[str, int]]) -> str:
    oldest_year = people[0][1]
    name = people[0][0]
    for person in people:
        if person[1] < oldest_year:
            oldest_year = person[1]
            name = person[0]

    return name


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))

    people_list = [("Arthur", 1977), ("Emily", 2014)]
    result = oldest_person(people_list)
    print(result)
