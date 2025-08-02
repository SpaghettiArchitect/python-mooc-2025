items = []
times = int(input("How many items: "))
i = 0
while i < times:
    item = int(input(f"Item {i + 1}: "))
    items.append(item)
    i += 1
print(items)
