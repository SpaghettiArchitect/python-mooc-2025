def main() -> None:
    phone_book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        elif command == 2:
            name = input("name: ")
            phone_number = input("number: ")
            if name not in phone_book:
                phone_book[name] = []
            phone_book[name].append(phone_number)
            print("ok!")
        else:
            name = input("name: ")
            if name not in phone_book:
                print("no number")
            else:
                for phone in phone_book[name]:
                    print(phone)


main()
