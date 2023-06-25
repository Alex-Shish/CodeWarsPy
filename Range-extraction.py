# Range Extraction
"""A format for expressing an ordered list of integers is to use a comma separated list of either
individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# '-6,-3-1,3-5,7-11,14,15,17-20'"""

def solution(args):
    arr = []
    st, i, k = args[0], 0, len(args)
    while i < k:
        st, j = args[i], i
        while j < k - 1 and args[j + 1] == args[j] + 1:
            j += 1
        if j - i > 1:
            st = str(args[i]) + "-" + str(args[j])
            i = j + 1
        else:
            i = (j if j > i else i + 1)
        arr.append(st)
    return ",".join(str(el) for el in arr)

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
