#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(p):
    k = 0
    b = 2
"""Variables Declared"""
while p > 1:
while p % b == 0:
    k += b
    p /= b
    b +=1
"""Arthimetic operations done"""
    return k
