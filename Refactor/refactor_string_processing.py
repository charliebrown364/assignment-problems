string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
split_string = string.split('\n')
strings = [x.split(',') for x in split_string]
length_of_string = len(string)

arr = []
for string in strings:
    new_string = []

    for char in string:
        
        if char[0] == '"' and char[-1] == '"':
            char = char[1:len(char) - 1]
        elif '.' in char:
            char = float(char)
        else:
            char = int(char)

        new_string.append(char)

    arr.append(new_string)

assert arr == [['alpha', 'beta', 'gamma', 'delta'], [1, 2, 3, 4], [5.0, 6.0, 7.0, 8.0]]
print("passed")