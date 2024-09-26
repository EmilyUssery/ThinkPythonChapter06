#!/usr/bin/env python
import sys

# System module allows us to tweak the recursion depth
sys.setrecursionlimit(10000)  # Default recursion depth is 1000

def ackermann(m, n):
    global count
    count += 1
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

count = 0
print(ackermann(2, 2))  # Prints 7
print( count )

count=0
print(ackermann(3, 3))  # Prints 61, but shows beyond exponential growth in recursive calls.
print( count )

# Even 4, 4 is WAY beyond 10000
print(ackermann(4, 4))  # Prints 7

print(ackermann(5, 5))  # Causes: RecursionError: maximum recursion depth exceeded
print(count)
""" This means so many function calls were made, that the limit set on recursion
were reached or the program wasn't allowed to get more memory."""