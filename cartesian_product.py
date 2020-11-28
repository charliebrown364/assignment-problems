def cartesian_product(arrays):
    
    ans = arrays[0]
    for i in range(1, len(arrays)):
        ans = [[a, b] for a in ans for b in arrays[i]]

    for i in range(len(arrays) - 1):
        ans = [elem for smaller_list in ans for elem in smaller_list]

    real_ans = []
    for elem_index in range(len(ans) // len(arrays)):
        real_ans.append([ans[len(arrays) * elem_index + i] for i in range(len(arrays))])
    
    if len(real_ans) == 1:
        return real_ans[0]
    else:
        return real_ans

assert cartesian_product([['a'], [1, 2, 3], ['Y', 'Z']]) == [['a',1,'Y'], ['a',1,'Z'], ['a',2,'Y'], ['a',2,'Z'], ['a',3,'Y'], ['a',3,'Z']]
print("passed")