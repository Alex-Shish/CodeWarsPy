# Snail
"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

def snail(snail_map):
    arr = []
    while len(snail_map) > 0:
        arr += snail_map[0]
        del snail_map[0]
        if len(snail_map) > 0:
            for i in snail_map:
                arr += [i[-1]]
                del i[-1]
            if snail_map[-1]:
                arr += snail_map[-1][::-1]
                del snail_map[-1]
            for i in reversed(snail_map):
                arr += [i[0]]
                del i[0]
    return arr

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
print(snail([[1,2,3],
             [8,9,4],
             [7,6,5]]))  # [1,2,3,4,5,6,7,8,9]
