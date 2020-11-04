import math

def single_var_gradient_descent(f, x, alpha = 0.01, delta = 0.0001, num_iterations = 10000):
    
    for i in range(num_iterations):
        derivative = (f(x + 0.5 * delta) - f(x - 0.5 * delta))/delta
        x = x - (alpha * derivative)

    return f(x)

def f(x):
    return 1 - x**2

print(single_var_gradient_descent(f, 1))

def gradient_descent(f, initial_point, alpha = 0.01, delta = 0.0001, num_iterations = 10000):
    x = initial_point[0]
    y = initial_point[1]
    
    for i in range(num_iterations):

        old_x = x
        old_y = y

        partial_x_derivative = (f(old_x + 0.5 * delta, old_y) - f(old_x - 0.5 * delta, old_y))/delta
        x = old_x - (alpha * partial_x_derivative)

        partial_y_derivative = (f(old_x, old_y + 0.5 * delta) - f(old_x, old_y - 0.5 * delta))/delta
        y = old_y - (alpha * partial_y_derivative)
    
    return f(x, y)

def f(x, y):
    return 1 + x**2 + y**2

# part a
"""
The minimum of f(x, y) = 1 + x^2 + y^2 is f(x, y) = 1. This occurs at the point (0, 0).
"""

# part b
print(gradient_descent(f, (1, 2)))

def f(x, y):
    return 1 + x**2 + 2*x + y**2 + 9*y

# part c
"""

f(x, y) = x^2 + 2x + y^2 - 9y + 1
= (x^2 + 2x) + (y^2 - 9y) + 1

x:
  ∂f/∂x = 2x + 2

  ∂f/∂x = 0
  2x + 2 = 0
  x = -1

y:
  ∂f/∂y = 2y - 9

  ∂f/∂y = 0
  2y - 9 = 0
  y = 9/2 = 4.5

minimum point of f(x, y) = (-1, 4.5)

f(-1, 4.5) = (-1)^2 + 2*(-1) + (4.5)^2 - 9*4.5 + 1 = 1 - 2 + 20.25 - 40.5 + 1 = -20.25

minimum of f(x, y) = f(-1, 4.5) = -20.25

"""

# part d
print(gradient_descent(f, (0, 0)))