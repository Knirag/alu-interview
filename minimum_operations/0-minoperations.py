#!/usr/bin/python3
"""Minimum Operations:Returns an integer"""

def minOperations(n):
    """Variables Declared"""
    k = 0
    b = 2
while n > 1:
    while n % b == 0:
    k += b
    n /= b
b +=1

return k
