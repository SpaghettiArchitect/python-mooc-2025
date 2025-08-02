items = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    items.append(item)
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)}")
