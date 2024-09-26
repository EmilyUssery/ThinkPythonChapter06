#!/usr/bin/env python3

def is_between(x, y, z):
    return (x < y < z) or (z < y < x);

# Test scenario 1, expect True
print(is_between(3, 4, 5))
# Test scenario 2, expect True
print(is_between(5, 4, 3))
# Test scenario 3, expect False
print(is_between(4, 3, 5))