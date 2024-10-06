#!/usr/bin/python3
"""
   Pascal's Triangle returns list of lists of n integers
   representing pascal's traingle of n integers

"""


def pascal_triangle(n):
    '''
        returns a list of lists of integers representing
        the Pascal’s triangle of n:
    '''

    pascals_list = [[1], [1, 1]]
    list_to_append = []  # Denotes the nested list
    sum = 0  # Hold sum of list elements

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    row_counter = 1  # working from row 1
    list_column_counter = 0  # to iterate in each list elements

    while row_counter <= n - 2:
        list_to_append.append(1)  # Insert 1 at the beginning of the list
        while list_column_counter <= row_counter - 1:
            sum = pascals_list[row_counter][list_column_counter] +
            pascals_list[row_counter][list_column_counter + 1]
            list_to_append.append(sum)
            list_column_counter += 1
        list_to_append.append(1)  # Insert 1 at the end of the list
        pascals_list.append(list_to_append)  # Append the new row list
        list_to_append = []  # Reset for each new iteration
        sum = 0
        row_counter += 1
        list_column_counter = 0
    return pascals_list
