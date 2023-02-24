#!/usr/bin/python3

"""
Rain program
"""

def rain(walls)

result = 0
if len(walls) == 0:
return 0
for s in range(1, len(walls) - 1):
k = walls[s]
b = walls[s]
for l in range(s):
k = max(k, walls[l])
for l in range(s + 1, len(walls)):
b = max(b, walls[l])
result = result +(min(a, b) - walls[s])
return result
