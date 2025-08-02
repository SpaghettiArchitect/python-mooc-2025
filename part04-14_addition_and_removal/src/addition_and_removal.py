items = []
sum = 1
while True:
    print(f"The list is now {items}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "x":
        print("Bye!")
        break
    elif command == "d":
        items.append(sum)
        sum += 1
    elif command == "r":
        items.pop()
        sum -= 1
