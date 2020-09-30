def minimum(num_list):
    smallest_num = num_list[0]
    for num in num_list:
        if smallest_num > num:
            smallest_num = num
    return smallest_num

def tally_sort(num_list):
    min_num = minimum(num_list)
    min_num_list = [num_list[num_index] - min_num for num_index in range(len(num_list))]

    tally_list = []
    for num_index in range(len(min_num_list)):
        num_of_nums = 0
        for num in min_num_list:
            if num == num_index:
                num_of_nums += 1
        tally_list.append(num_of_nums)

    sorted_tally_list = []
    for num_index in range(len(min_num_list)):
        for i in range(tally_list[num_index]):
            sorted_tally_list.append(num_index + min_num)

    return sorted_tally_list

print("\nTesting tally_sort([2, 5, 2, 3, 8, 6, 3])...")
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8], tally_sort([2, 5, 2, 3, 8, 6, 3])
print("PASSED")