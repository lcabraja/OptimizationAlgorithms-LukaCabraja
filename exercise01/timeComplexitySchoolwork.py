import time
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)
"""
Fill in with code. This function should have time complexity 
of O(n). The time needed to execute this function is linearly
dependent to input size (n).
n is a list of certian size.
"""


def linearFunction(n):
    for i in n:
        noop = i + i


"""
Fill in with code. This function should have time complexity 
of O(n^2). The time needed to execute this function is exponentionally
dependent to input size (n).
n is a list of certian size.
"""


def squareFunction(n):
    for i in n:
        for j in n:
            noop = i + j


"""
Fill in with code. This function should have time complexity 
of O(n!). The time needed to execute this function is factorially
dependent to input size (n).
n is a list of certian size.
"""


def factorialFunction(n):
    if len(n) == 1:
        return 1
    for i, j in enumerate(n):
        linearFunction(n[:i])


"""
DO NOT CHANGE THE CODE BELLOW.
THIS IS TESTING THE TIME COMPLEXITY AND 
MAKING BASIC PLOTS
"""
n_size_lin = []
time_list_lin = []
for size in range(100, 10000, 50):
    start = time.time()
    s = linearFunction(np.random.rand(size, 1))
    end = time.time()
    time_list_lin.append(end - start + 1)
    n_size_lin.append(size)


n_size_quad = []
time_list_quad = []
for size in range(100, 1000, 200):
    start = time.time()
    s = squareFunction(np.random.rand(size, 1))
    end = time.time()
    time_list_quad.append(end - start + 1)
    n_size_quad.append(size)


n_size_fact = []
time_list_fact = []
for size in range(100, 3000, 100):
    start = time.time()
    s = factorialFunction(*[range(2, size)])
    end = time.time()
    time_list_fact.append(end - start + 1)
    n_size_fact.append(size)

plt.plot(n_size_lin, time_list_lin, label="Linear")
plt.plot(n_size_quad, time_list_quad, label="Quadratic")
plt.plot(n_size_fact, time_list_fact, label="Factorial")
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.show()
