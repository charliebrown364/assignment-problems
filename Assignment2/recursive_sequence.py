# python recursive_sequence.py

#part a
def first_n_terms(n):
  ans = [5]
  for num in range(n - 1):
    ans.append((3 * ans[-1]) - 4)
  return ans

print('Testing first_n_terms on the input {}...'.format([5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051]))
assert first_n_terms(10) == [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051]
print('PASSED')

#part b
def nth_term(n):
  if n == 1:
    return 5
  else:
    return (3 * nth_term(n - 1)) - 4

print('Testing nth_term on the input {}...'.format(10))
assert nth_term(10) == 59051
print('PASSED')

# Quiz 1
def nth_term(n):
    if n == 2:
        return 3
    elif n == 1:
        return 0
    else:
        return nth_term(n - 1) - (2 * nth_term(n - 2))

# nth_term(6)
# nth_term(5) - (2 * nth_term(4))
# nth_term(4) - (2 * nth_term(3)) - (2 * nth_term(4))
# nth_term(3) - (2 * nth_term(2)) - (2 * nth_term(3)) - (2 * nth_term(4))
# nth_term(2) - (2 * nth_term(1)) - (2 * nth_term(2)) - (2 * nth_term(3)) - (2 * nth_term(4))
# 3 - (2 * 0) - (2 * 3) - (2 * nth_term(3)) - (2 * nth_term(4))
# -3 - (2 * nth_term(3)) - (2 * nth_term(4))
# -3 - (2 * (nth_term(2) - (2 * nth_term(1))))) - (2 * nth_term(4))
# -3 - (2 * (3 - (2 * 1)))) - (2 * nth_term(4))
# -5 - (2 * nth_term(4))
# -5 - (2 * (nth_term(3) - (2 * nth_term(2)))))
# -5 - (2 * ((nth_term(2) - (2 * nth_term(1))) - (2 * nth_term(2)))))
# -5 - (2 * ((3 - (2 * 0)) - (2 * 3))))
# 1

print("\nQuiz 1:")
print(nth_term(5)) # should equal 1