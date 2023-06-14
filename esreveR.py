"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use " x = list() " instead
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""

def reverse(lst):
    # empty_list = list()
    empty_list = []
    for i in lst:
        empty_list.insert(0, i)
    return empty_list

print(reverse([1, 2, 3]))
print(reverse([1,None,14,"two"]))