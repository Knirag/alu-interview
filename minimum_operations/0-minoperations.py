#!/usr/bin/python3
"""Minimum Operations:Returns an integer"""

def minOperations(n):
    """Variables Declared"""
 if n<=1:
    return 0

for k in range(2,int((n/2)+1)):
    id n % k ==0:
   return minOperations(int(n/i)) + k

return n
