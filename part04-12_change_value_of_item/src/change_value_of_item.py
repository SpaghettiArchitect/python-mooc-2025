values = [1, 2, 3, 4, 5]

index = 0
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    new_value = int(input("New value: "))
    values[index] = new_value
    print(values)
