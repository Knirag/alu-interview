#!/usr/bin/python3
""" Pascal's Triangle Theory"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle up to the n-th row.
    """
    if n <= 0:
        return []  # empty list
    
    triangle = [[1]]  # start with the first row
    
    for i in range(1, n):
        prev_row = triangle[-1]  # get the previous row
        curr_row = [1]  # the current row starts with 1
        
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])  # compute the j-th element of the current row
        
        curr_row.append(1)  # the current row ends with 1
        triangle.append(curr_row)  # add the current row to the triangle
    
    return triangle

