def minimum(num_list):
    smallest_num = num_list[0]
    for num in num_list:
        if smallest_num > num:
            smallest_num = num
    return smallest_num

# take an input list and sort its elements from least to greatest by repeatedly finding the smallest element and moving it to a new list

def simple_sort(num_list):
        
    ans = []
 
    for this_many_times in range(len(num_list)):
        for num in num_list:
            
            smallest_num = minimum(num_list)

            if num == smallest_num:
                ans.append(smallest_num)
                del num_list[num_list.index(num)]
            
    return ans

print("Testing simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])...")
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])
print("PASSED")

# PART B

# sorts the list from least to greatest by repeatedly going through each pair of adjacent elements and swapping them if they are in the wrong order. 

# PROCESS:
# 1. push all numbers before the current number into the answer array
# 2. if the current number is bigger that the next number, push the next number into the answer array first. Then push the ucrrent number into the array.
# 3. push all the numbers after the next number into the answer array.
# 4. Repeat the process for len(num_list)^2 times or until answer array is fully swapped

def swap_sort(num_list):
    num_swaps = 0
    for this_thing in num_list:
        for num in range(len(num_list) - 1):
            if num_list[num] > num_list[num + 1]:
                num_list[num], num_list[num + 1] = num_list[num + 1], num_list[num]
                num_swaps += 1
    print("len(num_list): {}".format(len(num_list)))
    print("num_swaps: {}".format(num_swaps))
    return num_list

print("Testing swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2])...")
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8]
print("PASSED")