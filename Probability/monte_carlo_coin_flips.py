def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)

# part a
def probability(num_heads, num_flips):
    # total number of possible outcomes for num_flips flips
    total_number_of_outcomes = 2 ** num_flips

    # number of outcomes in which num_heads heads arise in num_flips flips
    num_outcomes_with_num_heads_in_num_flips = factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))

    return num_outcomes_with_num_heads_in_num_flips / total_number_of_outcomes

print("Testing probability(5,8)...")
assert probability(5, 8) == 0.21875, probability(5, 8)
print("PASSED")

# part b
from random import random

def rand(a, b):
    rand = random()
    if rand < 0.5:
        return a
    else:
        return b

def monte_carlo_probability(num_heads, num_flips):
    outcomes = [[rand('h', 't') for flips in range(num_flips)] for num in range(1000)]

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