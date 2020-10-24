def merge_sort(input_list):
    if len(input_list) > 1: # if the input list consists of more than one element:
        # break up the input list into its left and right halves
        # sort the left and right halves by recursively calling merge_sort
        # merge the two sorted halves
        # return the result
    else: # if the input list consists of only one element, then it is already sorted,
        and you can just return it.

assert merge_sort([4, 8, 7, 7, 4, 2, 3, 1]) == [1, 2, 4, 5, 6, 7, 8, 9]