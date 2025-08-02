class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_common = my_list[0]
        total_repetitions = 0

        for item in my_list:
            repetitions = my_list.count(item)
            if repetitions > total_repetitions:
                total_repetitions = repetitions
                most_common = item

        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        unique_items = []
        total_doubles = 0

        for item in my_list:
            if item not in unique_items:
                unique_items.append(item)
                if my_list.count(item) >= 2:
                    total_doubles += 1

        return total_doubles
