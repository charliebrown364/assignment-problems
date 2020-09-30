def card_sort(num_list):
    ans = []

    for num in num_list:

        if len(ans) == 0:
            ans.append(num)
        else:

            before_ans = ans
            for sorted_num_index in range(len(ans)):
                if num > ans[::-1][sorted_num_index]:
                    ans = ans[:(len(ans) - sorted_num_index)] + [num] + ans[(len(ans) - sorted_num_index):]
                    break
            if before_ans == ans:
                ans = ans[:0] + [num] + ans[0:]

    return ans          

print("Testing card_sort([12, 11, 13, 5, 6])...")
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13], card_sort([12, 11, 13, 5, 6])
print("PASSED")

print("Testing card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1])...")
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7], card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1])
print("PASSED")