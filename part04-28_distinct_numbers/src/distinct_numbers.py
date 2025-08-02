def distinct_numbers(nums: list[int]) -> list[int]:
    unique_nums = []
    for num in sorted(nums):
        if len(unique_nums) == 0 or unique_nums[-1] != num:
            unique_nums.append(num)
    return unique_nums


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
