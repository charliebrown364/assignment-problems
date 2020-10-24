import math

def gradient_descent(f, x, alpha = 0.01, delta = 0.0001, iterations = 10000):
    for i in range(iterations):
        f_prime = (f(x + 0.5 * delta) - f(x - 0.5 * delta))/delta
        x = x - (alpha * f_prime)
    return f(x)

def g(x):
    return x**2 + 2*x + 1

print(gradient_descent(g, 0))

def h(x):
    return (x**2 + math.cos(x)) / (math.e ** math.sin(x))

print(gradient_descent(h, 0))