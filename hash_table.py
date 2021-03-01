buckets = [[], [], [], [], []]
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def hash_function(string):
    alphabet_dict = {alphabet[i]:i for i in range(len(alphabet))}
    total = 0
    for char in string:
        total += alphabet.index(char)
    return total % 5

def insert(buckets, key, value):
    pair = (key, value)
    bucket_index = hash_function(key)
    buckets[bucket_index].append(pair)

def find(buckets, key):
    bucket_index = hash_function(key)
    for bucket in buckets:
        for pair in bucket:
            if pair[0] == key:
                return pair[1]

for i, char in enumerate(alphabet):
    key = 'someletters' + char
    value = [i, i**2, i**3]
    insert(buckets, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters' + char
    output_value = find(buckets, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value

print("passed all")