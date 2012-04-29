from memoized import memoized
from math import sqrt

@memoized
def mfibonacci(num = 0):
    if num in (0, 1):
        return num
    return mfibonacci(num-1) + mfibonacci(num-2)

def fibonacci(num):
    if num in (0, 1):
        return num
    return fibonacci(num-1) + fibonacci(num-2)

def power_of(x, y, z):
    return (x**y)**z

@memoized
def mpower_of(x, y, z):
    return (x**y)**z

def solve_quadratic(a, b, c):
    return  (-b + sqrt(b**2 - 4*a*c))/(2*a)

@memoized
def msolve_quadratic(a, b, c):
    return  (-b + sqrt(b**2 - 4*a*c))/(2*a)

