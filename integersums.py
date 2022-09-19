# /usr/bin/env python

'''
    Problem Description:
    Sum of Integers Up To n (integersums.py)
    Write a function, add_it_up(), that takes a single integer as input 
    and returns the sum of the integers from zero to the input parameter.
    The function should return 0 if a non-integer is passed in.
'''

def add_it_up(integer):
    if not isinstance(integer, int):
        return 0
    
    return sum(range(integer+1))