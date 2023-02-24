#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
  Calculate how much water will be retained after a rainstorm using a list of non-negative integers that represent walls of width 1    """
    k = len(walls)
    if k == 0:
        return 0
    left_max = [0] * k
    right_max = [0] * k    left_max[0] = walls[0]
    for s in range(1, k):
        left_max[s] = max(left_max[s - 1], walls[s])
     right_max[k - 1] = walls[k - 1]
    for i in range(k - 2, -1, -1):
        right_max[s] = max(right_max[s + 1], walls[s])
    water = 0
     for s in range(k):
        water += min(left_max[s], right_max[s]) - walls[s]
    return water
