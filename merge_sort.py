def merge(x, y):
    ans = []
    for i in range(len(x) + len(y)):
        x_min = min(x) if len(x) > 0 else 1000
        y_min = min(y) if len(y) > 0 else 1000
        minimum = x_min if x_min < y_min else y_min
        current_list = x if minimum == x_min else y
        ans.append(minimum)
        del current_list[current_list.index(minimum)]
    return ans

print("Testing merge_sort...")
assert merge([-2,1,4,4,4,5,7], [-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7], merge([-2,1,4,4,4,5,7], [-1,6,6])
print("passed")