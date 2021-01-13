import math

def p(x):
    return (math.e ** ((-(x ** 2)) / 2)) / ((2 * math.pi) ** (1/2))

def calc_standard_normal_probability(a, b):
    ans = 0
    step_size = 0.001
    
    for i in range(1000*a, 1000*b):
        ans += step_size * p(i / 1000)
    
    return ans

print(calc_standard_normal_probability(-1, 1)) # should be 0.68
print(calc_standard_normal_probability(-2, 2)) # should be 0.955
print(calc_standard_normal_probability(-3, 3)) # should be 0.997