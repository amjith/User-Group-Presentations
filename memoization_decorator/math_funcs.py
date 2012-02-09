from memoized import memoized
from math import sqrt

@memoized
def mfibonacci(num):
    print 'fibonacci(%d)'%num
    if num == 0:
        return 0
    elif num ==1:
        return 1
    return mfibonacci(num-1) + mfibonacci(num-2)

def fibonacci(num):
    print 'fibonacci(%d)' %num
    if num == 0:
        return 0
    elif num ==1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

def power_of(x,y,z):
    return (x**y)**z

@memoized
def mpower_of(x,y,z):
    return (x**y)**z

def solve_quadratic(a,b,c):
    return  (-b + sqrt(b**2 - 4*a*c))/(2*a)

@memoized
def msolve_quadratic(a,b,c):
    return  (-b + sqrt(b**2 - 4*a*c))/(2*a)

