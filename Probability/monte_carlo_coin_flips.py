def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)

# part a
def probability(h, f):
    num_outcomes = 2 ** f
    num_outcomes_with_h_in_f = factorial(f) / (factorial(h) * factorial(f - h))
    return num_outcomes_with_h_in_f / num_outcomes

print("Testing probability(5,8)...")
assert probability(5, 8) == 0.21875, probability(5, 8)
print("PASSED")

# part b
from random import random

def monte_carlo_probability(num_heads, num_flips):
    outcomes = [[['h', 't'][round(random())] for flips in range(num_flips)] for num in range(1000)]

    times_it_was_correct = 0
    for outcome in outcomes:
        actual_num_heads = 0
        for result in outcome:
            if result == 'h':
                actual_num_heads += 1
        if actual_num_heads == num_heads:
            times_it_was_correct += 1

    return times_it_was_correct / 1000

# part c
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))