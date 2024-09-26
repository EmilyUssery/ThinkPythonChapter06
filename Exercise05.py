#!/usr/bin/env python

def gcd(a, b):
    """Recursive version to calculate the greatest common divisor."""
    if b == 0: return a
    return gcd(b, a % b)

def gcd_e(a, b):
    """More efficient looping version"""
    while b != 0:
        r = a % b
        a, b = b, r
    return a


print(gcd(85, 20))
print(gcd_e(85, 20))