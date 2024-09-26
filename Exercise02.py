#!/usr/bin/env python3
import math


def hypot_in0():
    return 0

print(f"hypot_in0 -> returns: {hypot_in0()}")

def hypot_in1(leg1, leg2):
    print( f"   parameters: l1:{leg1} l2:{leg2}")
    return 0

l1, l2 = 3, 4
print(f"l1:{l1} l2:{l2} hypot_in1 -> returns: {hypot_in1(l1, l2)}")

def hypot_in2(leg1, leg2):
    print( f"   parameters: l1:{leg1} l2:{leg2}" )
    l1squared = leg1**2
    l2squared = leg2**2
    l1plusl2 = l1squared + l2squared
    hypotenuse = math.sqrt(l1plusl2)
    print(f"    l1:{l1squared} l2:{l2squared} l1+l2:{l1plusl2} h:{hypotenuse}")
    return hypotenuse

l1, l2 = 3, 4
print(f"l1:{l1} l2:{l2} hypot_in2 -> returns: {hypot_in2(l1, l2)}")

def hypot(leg1, leg2):
    """Final version of calculating hypotenuse of right triangle from other legs."""
    return math.sqrt(leg1**2 + leg2**2)

l1, l2 = 3, 4
print(f"l1:{l1} l2:{l2} hypot -> returns: {hypot(l1, l2)}")
